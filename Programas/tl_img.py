#!/usr/bin/env python
# -*- coding: windows-1252 -*-
'''
Created on 13/06/2013

@author: diego.hahn
'''

import re
import struct
import array
import os
import glob
import sys
import shutil
import tempfile
import mmap

from rhCompression import lzss, rle, huffman
from rhImages import images, bmp

__title__ = "Layton's Image Processor"
__version__ = "2.0"

DEBUG = 1

def gba2tuple(fd):
    rgb = struct.unpack('<H', fd.read(2))[0] & 0x7FFF
    rgb = map(lambda x,y: float((x >> y) & 0x1F)/31.0, [rgb]*3, [0,5,10])
    return rgb
    
def tuple2gba(color):
    r, g, b = map(lambda x: int(float(x)/255.0*31), color)
    color = ((b << 10) | (g << 5) | r ) & 0x7FFF
    return struct.pack('<H', color)

def scandirs(path):
    files = []
    for currentFile in glob.glob( os.path.join(path, '*') ):
        if os.path.isdir(currentFile):
            files += scandirs(currentFile)
        else:
            files.append(currentFile)
    return files

def unpackBackground( src, dst ):
    #bg_path = os.path.join(src, 'img')
    bg_path = src
    files = filter(lambda x: x.__contains__('.cimg'), scandirs(bg_path))
        
    for _, fname in enumerate(files):
        try:
            print fname
            
            path = fname[len(src):]
            fdirs = dst + path[:-len(os.path.basename(path))]
            if not os.path.isdir(fdirs):
                os.makedirs(fdirs)          
            
            #fname = r"C:\WorkingCopy\playton-3\ROM Original\PLAYTON3\data\lt3\ani\uk\evt_chapt.cimg"
            file = open(fname, 'rb')
            type = struct.unpack('B', file.read(1))[0]
            if type == 0x30:
                buffer = rle.uncompress(file, 0)
            elif type == 0x10:     
                buffer = lzss.uncompress(file, 0)
            elif type == 0x24 or type == 0x28:
                buffer = huffman.uncompress(file, 0)
            else:
                file.seek(4,0)
                buffer = array.array('c', file.read())
               
            # with open("temp", "wb") as fd: fd.write(buffer.tostring())
            # raw_input()
               
            temp = mmap.mmap(-1, len(buffer))
            temp.write(buffer.tostring())
            file.close()

            temp.seek(0,0)
            assert temp.read(4) == "LIMG"
            colormap_offset = struct.unpack("<L", temp.read(4))[0]
            temp.read(8)
            tilemap_offset, tilemap_entries = struct.unpack("<HH", temp.read(4))
            background_offset, background_entries = struct.unpack("<HH", temp.read(4))
            colormap_type, colormap_entries = struct.unpack("<HH", temp.read(4))
            
            if colormap_type == 0 :
                colormap_bpp = 0
            else:
                colormap_bpp = 1

            width = struct.unpack('<H', temp.read(2))[0]
            height = struct.unpack('<H', temp.read(2))[0]   

            colormap = []
            tilelist = []
            buffer = array.array('c')
            
            temp.seek( colormap_offset )
            if colormap_type == 2 :
                for _ in range( 16**(1+colormap_bpp) - colormap_entries):
                    colormap.append((0,0,0))
                    
            for _ in range(colormap_entries):
                colormap.append(gba2tuple(temp))    

            temp.seek( background_offset )
            for _ in range(background_entries):
                tilelist.append(temp.read( 32 * 2**colormap_bpp ))                          

            temp.seek( tilemap_offset )
            for x in range(tilemap_entries):
                bytes = struct.unpack('<H', temp.read(2))[0]
                # v_mirror = bytes & 0x0800
                # h_mirror = bytes & 0x0400
                try:
                    string = tilelist[bytes & 0x3FF]
                except:
                    string = "\x00"*32*2**colormap_bpp
                # if v_mirror:
                    # string = vertical(string)
                # if h_mirror:
                    # string = horizontal(string)
                buffer.extend(string)
                       
            output = open(fdirs + os.path.basename(path) + '.bmp', 'wb')

            if colormap_bpp == 0:
                w = images.Writer((width, height), colormap, 4, 1, 0)
                w.write(output, buffer, 4, 'BMP')
            else:
                w = images.Writer((width, height), colormap, 8, 1, 0)
                w.write(output, buffer, 8, 'BMP')
            
            output.close()
        except AssertionError:
            pass
        except:
            pass
            
        temp.close()    
    
def packBackground( src, dst ):
    outdir = ['../Imagens/bg_pt/', '../Imagens/bg_pt/pt/']
    originals = ['../Imagens/bg/', '../Imagens/bg/en/']
    
    bg_path = os.path.join(src, 'bg')
    files = filter(lambda x: x.__contains__('.bmp'), scandirs(bg_path))    
    
    print "Buffering..."

    for name in files:    
                
        input = open(name, 'rb')
        w = images.Reader(input)
        data, colormap = w.as_data(mode = 1, bitdepth = 8)

        width = len(w.data[0])
        height = len(w.data)
        
        tilelist = []
        tileset = array.array('c')
        tilemap = array.array('c')
        
        for x in range(width*height/64):
            string = data[64*x:64*(x+1)]
            if string in tilelist:
                mapper = tilelist.index(string)
                tilemap.extend(struct.pack('<H', mapper))
            else:
                tilelist.append(string)
                mapper = tilelist.index(string)
                tileset.extend(string)
                tilemap.extend(struct.pack('<H', mapper))
            
        temp = open('temp', 'w+b')
        # Escrita do arquivo tempor?rio:
        temp.write(struct.pack('<L', 0xE0))#len(colormap)))
        for x in range(0xE0):#colormap:
            temp.write(tuple2gba(colormap[x]))
        temp.write(struct.pack('<L', len(tilelist)))
        tileset.tofile(temp)
        
        temp.write(struct.pack('<H', width / 8))
        temp.write(struct.pack('<H', height / 8))
        tilemap.tofile(temp)
        
        filepath = dst + name[len(src):]
        path  = os.path.dirname( filepath )
        if not os.path.isdir( path ):
            os.makedirs( path )                   
        
        output = open(filepath.replace('.bmp', ''), 'wb')
        output.write(struct.pack('<L', 2))
        
        buffer = lzss.compress(temp)             
        buffer.tofile(output)
        
        output.close()
        temp.close()
        
        print '>> \'' + filepath.replace('.bmp', '') + ' created.'
                
def unpackSprite( src, dst ):
    
    def r(f):
        txt = ""
        while True:
            b = f.read(1)
            if b == "\x00": return txt
            txt += b
    
    #ani_path = os.path.join(src, 'ani')
    ani_path = src
    files = filter(lambda x: x.__contains__('.cani') or x.__contains__('.arj'), scandirs(ani_path))
        
    for _, fname in enumerate(files):
            temp = open('temp', 'w+b')
        
        #try:
            print fname
            
            path = fname[len(src):]
            fdirs = dst + path[:-len(os.path.basename(path))]
            if not os.path.isdir(fdirs):
                os.makedirs(fdirs)                 
                        
            #fname = r"C:\WorkingCopy\playton-3\ROM Original\PLAYTON3\data\lt3\ani\uk\evt_chapt.cimg"
            file = open(fname, 'rb')
            type = struct.unpack('B', file.read(1))[0]
            if type == 0x30:
                buffer = rle.uncompress(file, 0)
            elif type == 0x10:     
                buffer = lzss.uncompress(file, 0)
            elif type == 0x24 or type == 0x28:
                buffer = huffman.uncompress(file, 0)
            else:
                file.seek(4,0)
                buffer = array.array('c', file.read())
                
            # with open("temp", "wb") as fd: fd.write(buffer.tostring())
            # raw_input()                
            
            temp = mmap.mmap(-1, len(buffer))
            temp.write(buffer.tostring())
            file.close()         

            temp.seek(0)
            header = struct.unpack("<7L", temp.read(7*4))
            # Verificações iniciais
            assert header[0] == 0x3243504c #"LPC2"
            # 0 u8 magic[4];
            # 1 u32 count;//Number of subfiles
            # 2 u32 dataStart;//The start of the file contents data
            # 3 u32 archiveFileSize;//The total size of the archive file, headers and padding included
            # 4 u32 fatOffset;//The position where the fat is located
            # 5 u32 fileNameBase;//The base value for file name pointers
            # 6 u32 fileContentsBase;//The base value for the file contents pointers
            
            for i in range( header[1] ):
                temp.seek( header[4] + i*12 )
                rec = struct.unpack("<3L", temp.read(3*4) )
                
                temp.seek( header[5] + rec[0] )
                name = r(temp)

                temp.seek( header[6] + rec[1] )
                content = temp.read(rec[2])
                
                if DEBUG:
                    with open( name, "wb") as fd:fd.write(content)
                
                print ">> " + name + " extracted"
                
                m = mmap.mmap(-1, len(content))
                m.write(content)
                m.seek(0)
                               
                stamp = m.read(4)
                if stamp == "LSCR":
                    header2 = struct.unpack("<HHLL", m.read(12))
                    with open(fdirs + os.path.basename(name) + '.txt', 'wb')   as fd:
                        for j in range( header2[0] ):
                            m.seek( header2[1] + j*8 )
                            rec2 = struct.unpack("<HHL", m.read(8))
                            if rec2[1] == 1:
                                continue
                            
                            elif rec2[1] == 3:
                                m.seek( header2[2] + rec2[2]*5 )
                                rec3 = struct.unpack("<BLBLBL", m.read(rec2[1]*5) )

                                m.seek( header2[3] + rec3[3] )
                                fd.write( "<HDR:" + "".join(map( lambda x: "%02X" % ord(x) , r(m)) ) + ">\n" )

                                m.seek( header2[3] + rec3[5] )
                                fd.write(r(m))
                                fd.write('\n!******************************!\n')
                                
                            else:
                                print "unsupported rec2[1] %d " % rec2[1]
                elif stamp == "LIMG":
                    colormap_offset = struct.unpack("<L", m.read(4))[0]
                    m.read(8)
                    tilemap_offset, tilemap_entries = struct.unpack("<HH", m.read(4))
                    background_offset, background_entries = struct.unpack("<HH", m.read(4))
                    colormap_type, colormap_entries = struct.unpack("<HH", m.read(4))
                    
                    if colormap_type == 0 :
                        colormap_bpp = 0
                    else:
                        colormap_bpp = 1

                    width = struct.unpack('<H', m.read(2))[0]
                    height = struct.unpack('<H', m.read(2))[0]   

                    colormap = []
                    tilelist = []
                    buffer = array.array('c')
                    
                    m.seek( colormap_offset )
                    if colormap_type == 2 :
                        for _ in range( 16**(1+colormap_bpp) - colormap_entries):
                            colormap.append((0,0,0))
                            
                    for _ in range(colormap_entries):
                        colormap.append(gba2tuple(m))    

                    m.seek( background_offset )
                    for _ in range(background_entries):
                        tilelist.append(m.read( 32 * 2**colormap_bpp ))                          

                    m.seek( tilemap_offset )
                    for x in range(tilemap_entries):
                        bytes = struct.unpack('<H', m.read(2))[0]
                        # v_mirror = bytes & 0x0800
                        # h_mirror = bytes & 0x0400
                        try:
                            string = tilelist[bytes & 0x3FF]
                        except:
                            string = "\x00"*32*2**colormap_bpp
                        # if v_mirror:
                            # string = vertical(string)
                        # if h_mirror:
                            # string = horizontal(string)
                        buffer.extend(string)
                               
                    output = open(fdirs + os.path.basename(path) + '.bmp', 'wb')

                    if colormap_bpp == 0:
                        w = images.Writer((width, height), colormap, 4, 1, 0)
                        w.write(output, buffer, 4, 'BMP')
                    else:
                        w = images.Writer((width, height), colormap, 8, 1, 0)
                        w.write(output, buffer, 8, 'BMP')
                    
                    output.close()
                else:
                    print "unsupported stamp %s " % stamp
                   
                m.close()
            # if re.match(r'^.*\.cani$', name):
                # temp.seek(0,0)
                # entries = struct.unpack('<H', temp.read(2))[0]
                # type = struct.unpack('<H', temp.read(2))[0]
                # objs = []
                
                # if type == 3:
                    # for p in range(entries):
                        # xcoord = struct.unpack('<H', temp.read(2))[0]
                        # ycoord = struct.unpack('<H', temp.read(2))[0]
                        # obj_entries = struct.unpack('<L', temp.read(4))[0]
                        
                        # objs_params = []
                        
                        # for x in range(obj_entries):
                            # obj_xcoord = struct.unpack('<H', temp.read(2))[0]
                            # obj_ycoord = struct.unpack('<H', temp.read(2))[0]          
                            # obj_width = 4 * (2 ** struct.unpack('<H', temp.read(2))[0]) # 4 BPP)
                            # obj_height = 8 * (2 ** struct.unpack('<H', temp.read(2))[0])
                            # obj_data = []

                            # for y in range(obj_height):
                                # obj_data.append(f.read(obj_width))
                                
                            # objs_params.append( (obj_xcoord, obj_ycoord,
                                                 # obj_width, obj_height, obj_data) )

                        # width = 0
                        # height = 0

                        # for obj_param in objs_params:
                            # if width <= obj_param[0] + obj_param[2]*2:
                                # width = obj_param[0] + obj_param[2]*2
                            # if height <= obj_param[1] + obj_param[3]:
                                # height = obj_param[1] + obj_param[3]

                        # buffer = array.array('c', '\xFF' * width * height)

                        # for obj_param in objs_params:
                            # obj_data = obj_param[4]
                            # for y in range(obj_param[3]):
                                # buffer[width/2*(obj_param[1] + y) + (obj_param[0])/2:
                                       # width/2*(obj_param[1] + y) + (obj_param[0])/2 + obj_param[2]] = array.array('c', obj_data.pop(0))                        

                        # objs.append((width, height, buffer))
                                       
                    # pal_entries = struct.unpack('<L', temp.read(4))[0]         
                    # colormap = []
                    # for x in range(pal_entries):
                        # colormap.append(gba2tuple(temp))

                    # for x in range(entries):                             
                        # output = open(os.path.join(fdirs, '%s-%02d-%02d.bmp' %(fname, (x+1), entries)), 'wb')
                        # w = images.Writer((objs[x][0], objs[x][1]), colormap, 4, 2)
                        # w.write(output, objs[x][2], 4, 'BMP')
                        # output.close()

                # elif type == 4:
                    # for p in range(entries):
                        # xcoord = struct.unpack('<H', temp.read(2))[0]
                        # ycoord = struct.unpack('<H', temp.read(2))[0]
                        # obj_entries = struct.unpack('<L', temp.read(4))[0]
                        
                        # objs_params = []                        

                        # for x in range(obj_entries):
                            # obj_xcoord = struct.unpack('<H', temp.read(2))[0]
                            # obj_ycoord = struct.unpack('<H', temp.read(2))[0]          
                            # obj_width = 8 * (2 ** struct.unpack('<H', temp.read(2))[0])
                            # obj_height = 8 * (2 ** struct.unpack('<H', temp.read(2))[0])
                            # obj_data = []
                            # for y in range(obj_height):
                                # obj_data.append(temp.read(obj_width))                          

                            # objs_params.append( (obj_xcoord, obj_ycoord,
                                                 # obj_width, obj_height, obj_data) )
                
                        # width = 0
                        # height = 0

                        # for obj_param in objs_params:
                            # if width <= obj_param[0] + obj_param[2]:
                                # width = obj_param[0] + obj_param[2]
                            # if height <= obj_param[1] + obj_param[3]:
                                # height = obj_param[1] + obj_param[3]                        

                        # buffer = array.array('c', '\xFF' * width * height)
                        
                        # for obj_param in objs_params:
                            # obj_data = obj_param[4]
                            # for y in range(obj_param[3]):
                                # buffer[width*(obj_param[1] + y) + (obj_param[0]):
                                       # width*(obj_param[1] + y) + (obj_param[0]) + obj_param[2]] = array.array('c', obj_data.pop(0))                        
                
                        # objs.append((width, height, buffer))

                    # pal_entries = struct.unpack('<L', f.read(4))[0]         
                    # colormap = []
                    # for x in range(pal_entries):
                        # colormap.append(gba2tuple(temp))                               
                        
                    # for x in range(entries):
                        # output = open(os.path.join(fdirs, '%s-%02d-%02d.bmp' %(fname, (x+1), entries)), 'wb')
                        # w = images.Writer((objs[x][0], objs[x][1]), colormap, 8, 2)
                        # w.write(output, objs[x][2], 8, 'BMP')
                        # output.close()                                                  
                    
                # else:
                    # print 'except %s' % name

            # elif re.match(r'^.*\.arj$', name):
                # f.seek(0,0)
                # objs = []
            
                # entries = struct.unpack('<H', f.read(2))[0]
                # type = struct.unpack('<H', f.read(2))[0]                        
                # pal_entries = struct.unpack('<L', f.read(4))[0]
                # for p in range(entries):
                    # xcoord = struct.unpack('<H', f.read(2))[0]
                    # ycoord = struct.unpack('<H', f.read(2))[0]
                    # obj_entries = struct.unpack('<L', f.read(4))[0]
                    
                    # objs_params = []
                    
                    # for x in range(obj_entries):
                        # obj_shape = struct.unpack('<H', f.read(2))[0]
                        # obj_size = struct.unpack('<H', f.read(2))[0]
                        # obj_xcoord = struct.unpack('<H', f.read(2))[0]
                        # obj_ycoord = struct.unpack('<H', f.read(2))[0]
                        # obj_width = 8 * (2**struct.unpack('<H', f.read(2))[0])
                        # obj_height = 8 * (2**struct.unpack('<H', f.read(2))[0]) 
                        # obj_data = []
                        # for y in range(obj_width * obj_height / 64):
                            # obj_data.append(f.read(64))
                            
                        # objs_params.append( (obj_shape, obj_size, obj_xcoord, obj_ycoord,
                                             # obj_width, obj_height, obj_data) )
                    # width = 0
                    # height = 0

                    # for obj_param in objs_params:
                        # if width <= obj_param[2] + obj_param[4]:
                            # width = obj_param[2] + obj_param[4]
                        # if height <= obj_param[3] + obj_param[5]:
                            # height = obj_param[3] + obj_param[5]
                                                                
                    # buffer = array.array('c', '\xFF' * width * height)
                    
                    # for obj_param in objs_params:
                        # obj_data = obj_param[6]
                        # for y in range(obj_param[5] / 8):
                            # for w in range(obj_param[4] / 8):
                                # buffer[(width*(obj_param[3] + y*8)) + obj_param[2]*8 + 64*(w):
                                       # (width*(obj_param[3] + y*8)) + obj_param[2]*8 + 64*(w+1)] = array.array('c',obj_data.pop(0))

                    # objs.append((width, height, buffer))
            
                # colormap = []
                # for _ in range(pal_entries):
                    # colormap.append(gba2tuple(f))

                # for x in range(entries):
                    # output = open(os.path.join(fdirs, '%s-%02d-%02d.bmp' %(fname, (x+1), entries)), 'wb')
                    # w = images.Writer((objs[x][0], objs[x][1]), colormap, 8, 1)
                    # w.write(output, objs[x][2], 8, 'BMP')
                    # output.close()
                    
        # except AssertionError:
            # pass
        # except:
            # pass
            
            temp.close()                     
                            
def packSprite( src, dst, src1 ):
    holder = {}

    # Passo 1 - Gerar um dicion?rio com todos os sprites a serem empacotados
    
    ani_path = os.path.join(src, 'ani')
    files = filter(lambda x: x.__contains__('.bmp'), scandirs(ani_path))    
    
    print "Buffering..."

    for name in files:
        print ">>> ", name
        a = re.match( r'(.*)-(.*)-(.*)\.bmp$', name[len(src):] )
        if a.group(1) not in holder:
            holder.update({a.group(1):{}})#[]})
            
        w = bmp.Reader( name )
        d = w.read()
        p = w.read_palette()
        w.file.close()
        holder[a.group(1)].update({int(a.group(2)) - 1: (d,p)})#append((d, p))
        
    print "Analyzing..."       
        
    compressions = {}
    data = {}
    # Passo 2 - Descompactar os arquivos originais
    for name in holder.keys():  
        file = open( src1 + name , "rb")
        type = struct.unpack('<L', file.read(4))[0]
        if type == 1:
            buffer = rle.uncompress(file, 0x4)
        elif type == 2:     
            buffer = lzss.uncompress(file, 0x4)
        elif type == 3 or type == 4:
            buffer = huffman.uncompress(file, 0x4)
        else:
            file.seek(0,0)
            buffer = array.array('c', file.read())
        compressions.update({name:type})
        file.close()

        data.update( {name:buffer} )
                
    # Passo 3 - Atualizar os containers com os novos sprites
    #for i, dir in enumerate(outdir):
    for name in data.keys():
        print "Updating ", name
        buffer = data[name]
        arrays = []
        with open( "temp", "w+b") as f:
            buffer.tofile( f )            
            f.seek(0,0)
            if re.match(r'^.*\.arc$', name):
                entries = struct.unpack("<H", f.read(2))[0]
                bitdepth = 2 ** (struct.unpack("<H", f.read(2))[0] - 1)
                for x in range(entries):
                    sprite_data = holder[name][x][0]
                    sprite_pal = holder[name][x][1]
                    # Leitura do header do sprite
                    f.seek(4, 1) # As coordenadas n?o ser?o mudadas a principio
                    obj_entries = struct.unpack("<L", f.read(4))[0]
                    for y in range(obj_entries):
                        xpos = struct.unpack("<H", f.read(2))[0]
                        ypos = struct.unpack("<H", f.read(2))[0]
                        width = 8 * (2 ** struct.unpack("<H", f.read(2))[0])
                        height = 8 * (2 ** struct.unpack("<H", f.read(2))[0])
                        obj = []
                        for w in range(height):
                            obj.append(sprite_data[ypos + w][xpos:xpos + width])

                        bitarray = array.array('B')
                        for row in obj:
                            if bitdepth < 8:
                                row = zip(*[iter(row)]*(8/bitdepth))
                                row = map(lambda e: reduce(lambda x,y:(x << bitdepth) + y, reversed(e)), row)
                            bitarray.extend(row)
                            
                        arrays.append((f.tell(), array.array("c", bitarray.tostring())))
                        f.seek(len(bitarray.tostring()), 1)

                pal_entries = struct.unpack('<L', f.read(4))[0]
                
            elif re.match(r'^.*\.arj$', name): 
                entries = struct.unpack("<H", f.read(2))[0]
                bitdepth = 2 ** (struct.unpack("<H", f.read(2))[0] - 1)
                colors = struct.unpack("<L", f.read(4))[0]
                for x in range(entries):
                    sprite_data = holder[name][x][0]
                    sprite_pal = holder[name][x][1]
                    
                    sprite_xpos = struct.unpack("<H", f.read(2))[0]
                    sprite_ypos = struct.unpack("<H", f.read(2))[0]
                    obj_entries = struct.unpack("<L", f.read(4))[0]
                    
                    for y in range(obj_entries):
                        obj_shape = struct.unpack('<H', f.read(2))[0]
                        obj_size = struct.unpack('<H', f.read(2))[0]
                        obj_xcoord = struct.unpack('<H', f.read(2))[0]
                        obj_ycoord = struct.unpack('<H', f.read(2))[0]
                        obj_width = 2**struct.unpack('<H', f.read(2))[0]
                        obj_height = 2**struct.unpack('<H', f.read(2))[0]
                        
                        obj = [[list() for p in range(obj_width)] for t in range(obj_height)]

                        for ypos in range(obj_height):
                            for xpos in range(obj_width):
                                for w in range(8):
                                    obj[ypos][xpos] += (sprite_data[obj_ycoord + ypos*8 + w][obj_xcoord + xpos*8:obj_xcoord + xpos*8 + 8])
                            
                        bitarray = array.array('B')
                        for row in obj:
                            for d in row:
                                bitarray.extend(d)
                            
                        arrays.append((f.tell(), array.array("c", bitarray.tostring())))
                        f.seek(len(bitarray.tostring()), 1)
                        
        with open( "temp", "r+b") as f: 
            for par in arrays:
                f.seek(par[0], 0)
                par[1].tofile(f)                

                
# Passo 4
        print "Compressing..."

        with open( "temp", "rb") as f:
            type = compressions[name]
            if type == 1:
                buffer = rle.compress(f)
            elif type == 2:
                buffer = lzss.compress(f)
            elif type == 3:
                buffer = huffman.compress(f, 4)
            elif type == 4:
                buffer = huffman.compress(f, 8)

            filepath = dst + name
            path  = os.path.dirname( filepath )
            #print path
            if not os.path.isdir( path ):
                os.makedirs( path )               
                
            g = open( filepath, "wb")
            g.write(struct.pack("<L", type))
            buffer.tofile(g)
            g.close()
            
            print '>> \'' + filepath + ' created.'            
                            
if __name__ == "__main__":

    import argparse
    
    os.chdir( sys.path[0] )
    os.system( 'cls' )

    print "{0:{fill}{align}70}".format( " {0} {1} ".format( __title__, __version__ ) , align = "^" , fill = "=" )

    parser = argparse.ArgumentParser()
    parser.add_argument( '-m', dest = "mode", type = str, required = True )
    parser.add_argument( '-s', dest = "src", type = str, nargs = "?", required = True )
    parser.add_argument( '-s1', dest = "src1", type = str, nargs = "?" )
    parser.add_argument( '-d', dest = "dst", type = str, nargs = "?", required = True )
    
    args = parser.parse_args()
    
    # dump bg
    if args.mode == "e0":
        print "Unpacking background"
        unpackBackground( args.src , args.dst )
    # insert bg
    elif args.mode == "i0": 
        print "Packing background"
        packBackground( args.src , args.dst )
    # dump ani
    elif args.mode == "e1": 
        print "Unpacking animation"
        unpackSprite( args.src , args.dst )
    # insert ani
    elif args.mode == "i1": 
        print "Packing animation"
        print args.src1
        packSprite( args.src , args.dst , args.src1 )
    else:
        sys.exit(1)
