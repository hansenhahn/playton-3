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
__version__ = "3.0"

DEBUG = 0

def r(f):
    txt = ""
    while True:
        b = f.read(1)
        if b == "\x00": return txt
        txt += b

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

def unpackBackground( src, tmp, dst ):

    files = filter(lambda x: x.__contains__('.cimg'), scandirs(src))
        
    for _, fname in enumerate(files):
        try:
            print fname
            
            path = fname[len(src):]
            fdirs = dst + path[:-len(os.path.basename(path))]
            if not os.path.isdir(fdirs):
                os.makedirs(fdirs)
                
            ftemp = tmp + path[:-len(os.path.basename(path))]
            if not os.path.isdir(ftemp):
                os.makedirs(ftemp)   
            
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
            
            # vamos simplificar a inserção mantendo um tracking dos arquivos originais descomprimidos
            with open(ftemp + os.path.basename(path) , 'wb') as fd:
                fd.write(buffer.tostring())
 
               
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
    
def packBackground( src, tmp, dst ):

    files = filter(lambda x: x.__contains__('.bmp'), scandirs(src))    
    
    print "Buffering..."

    for fname in files:    
        print fname
        path = fname[len(src):]
        fdirs = dst + path[:-len(os.path.basename(path))]          
        ftemp = tmp + path[:-len(os.path.basename(path))]
              
        input = open(fname, 'rb')
        w = images.Reader(input)
        data, colormap = w.as_data(mode = 1)
        bitdepth = w._bitdepth
        tile_size = 8*bitdepth

        width = len(w.data[0])
        height = len(w.data)
        
        tilelist = []
        tileset = array.array('c')
        tilemap = array.array('c')
        
        for x in range(width*height/tile_size):
            string = data[tile_size*x:tile_size*(x+1)]
            if string in tilelist:
                mapper = tilelist.index(string)
                tilemap.extend(struct.pack('<H', mapper))
            else:
                tilelist.append(string)
                mapper = tilelist.index(string)
                tileset.extend(string)
                tilemap.extend(struct.pack('<H', mapper))
                
        with open(ftemp + os.path.basename(path).replace(".bmp", "") , 'rb') as fd:
            buffer = fd.read()
                              
        temp = open('temp', 'w+b')
        temp.write(buffer)

        temp.seek(0,0)
        assert temp.read(4) == "LIMG"
        colormap_offset = struct.unpack("<L", temp.read(4))[0]
        temp.read(8)
        tilemap_offset, tilemap_entries = struct.unpack("<HH", temp.read(4))
        
        # atualiza a quantidade de tiles 
        background_offset = struct.unpack("<H", temp.read(2))[0]
        temp.write(struct.pack("<H", len(tilelist)))
        
        colormap_type, colormap_entries = struct.unpack("<HH", temp.read(4))
        
        temp.seek( tilemap_offset )
        temp.write(tilemap.tostring())     

        temp.seek( background_offset )
        temp.write(tileset.tostring())     

        
        filepath = dst + fname[len(src):]
        path  = os.path.dirname( filepath )
        if not os.path.isdir( path ):
            os.makedirs( path )                   
        
        output = open(filepath.replace('.bmp', ''), 'wb')
       # output.write(struct.pack('<L', 2))
        
        buffer = lzss.compress(temp)             
        buffer.tofile(output)
        
        output.close()
        temp.close()
        
        print '>> \'' + filepath.replace('.bmp', '') + ' created.'
                
def unpackSprite( src, tmp, dst ):
        
    ani_path = src
    files = filter(lambda x: x.__contains__('.cani') or x.__contains__('.arj'), scandirs(ani_path))
        
    for _, fname in enumerate(files):
        
        #try:
            print fname
            
            path = fname[len(src):]
            fdirs = dst + path[:-len(os.path.basename(path))]
            if not os.path.isdir(fdirs):
                os.makedirs(fdirs)

            ftemp = tmp + path[:-len(os.path.basename(path))]
            if not os.path.isdir(ftemp):
                os.makedirs(ftemp)                 
                        
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
            with open(ftemp + os.path.basename(path) , 'wb') as fd:
                fd.write(buffer.tostring())
           
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
                if stamp == "LIMG":
                    colormap_offset = struct.unpack("<L", m.read(4))[0]
                    attr_offset, attr_entries = struct.unpack("<HH", m.read(4))
                    m.read(4)
                    tilemap_offset, tilemap_entries = struct.unpack("<HH", m.read(4))
                    background_offset, background_entries = struct.unpack("<HH", m.read(4))
                    colormap_type, colormap_entries = struct.unpack("<HH", m.read(4))
                    
                    if colormap_type == 0 :
                        colormap_bpp = 0
                    else:
                        colormap_bpp = 1

                    width = struct.unpack('<H', m.read(2))[0]
                    height = struct.unpack('<H', m.read(2))[0]   

                    attr = []
                    colormap = []
                    tilelist = []
                    buffer = array.array('c')
                    
                    m.seek( colormap_offset )
                    if colormap_type == 2 :
                        for _ in range( 16**(1+colormap_bpp) - colormap_entries):
                            colormap.append((0,0,0))
                            
                    for _ in range(colormap_entries):
                        colormap.append(gba2tuple(m))
                        
                    m.seek(attr_offset)
                    for _ in range(attr_entries):
                        x0, y0, w, h = struct.unpack("<BBBB", m.read(4))
                        m.read(4)
                        attr.append((x0<<3, y0<<3, w<<3, h<<3))
                    
                    m.seek( background_offset )
                    for _ in range(background_entries):
                        tilelist.append(m.read( 32 * 2**colormap_bpp ))                          

                    m.seek( tilemap_offset )
                    for x in range(tilemap_entries):
                        bytes = struct.unpack('<H', m.read(2))[0]
                        # v_mirror = bytes & 0x0800
                        # h_mirror = bytes & 0x0400
                        try:
                            string = tilelist[bytes]
                        except:
                            string = "\x00"*32*2**colormap_bpp
                        # if v_mirror:
                            # string = vertical(string)
                        # if h_mirror:
                            # string = horizontal(string)
                        buffer.extend(string)
                               
                    output = open(fdirs + os.path.basename(path) + ('-%02d.bmp' % (i)), 'wb')

                    if colormap_bpp == 0:
                        w = images.Writer((width, height), colormap, 4, 1, 0)
                        w.write(output, buffer, 4, 'BMP')
                    else:
                        w = images.Writer((width, height), colormap, 8, 1, 0)
                        w.write(output, buffer, 8, 'BMP')
                    
                    output.close()                    
                    
                    
                    try:
                        for j in range(attr_entries):
                            spr_buffer = array.array('c')
                            x0, y0, w, h = attr[j]
                            for hi in range(h/8):
                                if colormap_bpp == 0:
                                    spr_buffer.extend(buffer[width*(y0+hi*8)/2 + x0*4: width*(y0+hi*8)/2 + (x0+w)*4])
                                else:
                                    spr_buffer.extend(buffer[width*(y0+hi*8) + x0*8: width*(y0+hi*8) + (x0+w)*8])
                        
                            output = open(fdirs + os.path.basename(path) + ('-%02d-%02d-%02d.bmp' % (i, j+1, attr_entries)), 'wb')

                            if colormap_bpp == 0:
                                w = images.Writer((w, h), colormap, 4, 1, 0)
                                w.write(output, spr_buffer, 4, 'BMP')
                            else:
                                w = images.Writer((w, h), colormap, 8, 1, 0)
                                w.write(output, spr_buffer, 8, 'BMP')
                            
                            output.close()
                    except:
                        pass
                else:
                    print "unsupported stamp %s " % stamp
                   
                m.close()

            temp.close()                     
                            
def packSprite( src, tmp, dst ):
    holder = {}

    # Passo 1 - Gerar um dicion?rio com todos os sprites a serem empacotados    
    files = filter(lambda x: x.__contains__('.bmp'), scandirs(src))    
    
    print "Buffering..."    

    for fname in files:
        print ">>> ", fname
        a = re.match( r'(.*)-(.*)-(.*)-(.*)\.bmp$', fname[len(src):] )
        if a.group(1) not in holder:
            holder.update({a.group(1):{}})
        if int(a.group(2)) not in holder[a.group(1)]:
            holder[a.group(1)].update({int(a.group(2)):{}})            
            
        input = open(fname, 'rb')
        w = images.Reader(input)        
        data, colormap = w.as_data(mode = 1)        
        bitdepth = w._bitdepth
        w.file.close()

        holder[a.group(1)][int(a.group(2))].update({int(a.group(3)) - 1: (data, colormap, bitdepth)})
    
    print "Analyzing..."
        
    compressions = {}
    data = {}
    # Passo 2 - Bufferizar os arquivos originais
    for name in holder.keys():
        with open(tmp+name, 'rb') as fd:
            buffer = fd.read()
            data.update( {name:buffer} )
        
    # Passo 3 - Atualizar os containers com os novos sprites
    #for i, dir in enumerate(outdir):
    for name in data.keys():
        print "Updating ", name
        data_buffer = data[name]
        sprites = holder[name]
        arrays = []
        record = []        
        with open( "temp", "w+b") as f:
            f.write(data_buffer)
            f.seek(0,0)
            
            # lendo o cabeçalho do arquivo original bufferizado
            header = struct.unpack("<7L", f.read(7*4))
            # Verificações iniciais
            assert header[0] == 0x3243504c #"LPC2"
            # 0 u8 magic[4];
            # 1 u32 count;//Number of subfiles
            # 2 u32 dataStart;//The start of the file contents data
            # 3 u32 archiveFileSize;//The total size of the archive file, headers and padding included
            # 4 u32 fatOffset;//The position where the fat is located
            # 5 u32 fileNameBase;//The base value for file name pointers
            # 6 u32 fileContentsBase;//The base value for the file contents pointers
            for i in range(header[1]):           
                f.seek( header[4] + i*12 )
                rec = struct.unpack("<3L", f.read(3*4))
                
                f.seek( header[5] + rec[0] )
                #name = r(f)

                f.seek( header[6] + rec[1] )
                content = array.array("c", f.read(rec[2]))

                if i in sprites:                    
                    sprite_seq = sprites[i]                
                    
                    # conteudo
                    f.seek( header[6] + rec[1] )
                    offset = f.tell()
                    stamp = f.read(4)
                    if stamp == "LIMG":
                        colormap_offset = struct.unpack("<L", f.read(4))[0]
                        attr_offset, attr_entries = struct.unpack("<HH", f.read(4))
                        f.read(4)
                        tilemap_offset, tilemap_entries = struct.unpack("<HH", f.read(4))
                        background_offset, background_entries = struct.unpack("<HH", f.read(4))
                        colormap_type, colormap_entries = struct.unpack("<HH", f.read(4))
                        
                        if colormap_type == 0 :
                            colormap_bpp = 0
                        else:
                            colormap_bpp = 1

                        width = struct.unpack('<H', f.read(2))[0]
                        height = struct.unpack('<H', f.read(2))[0]
                        
                        attr = []
                        
                        raw_colormap = array.array('c')
                        tilelist = []
                        buffer = array.array('c')
                        
                        f.seek( offset+colormap_offset )
                        raw_colormap.extend(f.read(colormap_entries*2))
                        
                        # colormap = []
                        # f.seek( offset+colormap_offset )
                        # if colormap_type == 2 :
                            # for _ in range( 16**(1+colormap_bpp) - colormap_entries):
                                # colormap.append((0,0,0))
                                
                        # for _ in range(colormap_entries):
                            # colormap.append(gba2tuple(f))
                            
                        f.seek(offset+attr_offset)
                        for _ in range(attr_entries):
                            x0, y0, w, h = struct.unpack("<BBBB", f.read(4))
                            f.read(4)
                            attr.append((x0<<3, y0<<3, w<<3, h<<3))
                        
                        f.seek( offset+background_offset )
                        for _ in range(background_entries):
                            tilelist.append(f.read( 32 * 2**colormap_bpp ))                          

                        f.seek(offset+tilemap_offset )
                        for x in range(tilemap_entries):
                            bytes = struct.unpack('<H', f.read(2))[0]
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

                        # montamos o background original, agora vamos atualizá-lo com os sprites traduzidos
                        for j in range(attr_entries):
                            sprite_buffer = sprite_seq[j][0]
                            x0, y0, w, h = attr[j]
                            for hi in range(h/8):
                                if colormap_bpp == 0:
                                    line = sprite_buffer[:w*4]
                                    sprite_buffer = sprite_buffer[w*4:]
                                    for wi, l in enumerate(line):
                                        buffer[width*(y0+hi*8)/2 + x0*4 + wi] = l                                
                                else:
                                    line = sprite_buffer[:w*8]
                                    sprite_buffer = sprite_buffer[w*8:]
                                    for wi, l in enumerate(line):
                                        buffer[width*(y0+hi*8) + x0*8 + wi] = l
                                        
                        # desmontamos o background e geramos um novo tilemap
                        full_tileset = list()
                        if colormap_bpp == 0:
                            lenght = len(buffer) / 32
                            for x in range(lenght):
                                full_tileset.append(buffer[32*x:32*(x+1)].tostring())
                        else:
                            lenght = len(buffer) / 64
                            for x in range(lenght):
                                full_tileset.append(buffer[64*x:64*(x+1)].tostring())
                                
                        full_tileset.remove("\x00"*32*2**colormap_bpp)        

                        tiles = list(set(full_tileset))
                        new_tileset = array.array('c')
                        new_tilemap = array.array('c')
                        for tile in tiles:
                            new_tileset.extend(tile)
                        #print tiles
                        for tile in full_tileset:
                            if tile == "\x00"*32*2**colormap_bpp:
                                index = 0xffff
                            else:
                                index = tiles.index(tile)
                            #print index
                            new_tilemap.extend(struct.pack("<H", index))

                        while len(content) % 4 != 0:
                            content.extend('\x00')
                            
                        tilemap_offset = len(content)-1
                        tilemap_entries = len(new_tilemap) / 2
                        content.extend(new_tilemap.tostring())
                        while len(content) % 4 != 0:
                            content.extend('\x00')
                            
                        background_offset = len(content)
                        background_entries = len(new_tileset) / (32*2**colormap_bpp)
                        content.extend(new_tileset.tostring())
                        while len(content) % 4 != 0:
                            content.extend('\x00')
                        
                        content[16], content[17] = struct.pack("<H", tilemap_offset)
                        content[18], content[19] = struct.pack("<H", tilemap_entries)
                        content[20], content[21] = struct.pack("<H", background_offset)
                        content[22], content[23] = struct.pack("<H", background_entries)                        

                            
                        # output = open(os.path.basename(name) + ('-%02d.bmp' % (i)), 'wb')

                        # if colormap_bpp == 0:
                            # w = images.Writer((width, height), colormap, 4, 1, 0)
                            # w.write(output, buffer, 4, 'BMP')
                        # else:
                            # w = images.Writer((width, height), colormap, 8, 1, 0)
                            # w.write(output, buffer, 8, 'BMP')
                        
                        # output.close()                                               
                    
                    #return
                record.append(content)
                  
            # file content
            f.seek(header[6])
            # vamos atualizar os arquivos
            for i, content in enumerate(record):
                pointer = f.tell() - header[6]
                size = len(content)
                f.write(content)
                while f.tell() % 4 != 0: f.write('\x00')
                link = f.tell()
                
                f.seek(header[4] + i*12 + 4)
                f.write(struct.pack("<L", pointer))
                f.write(struct.pack("<L", size))
                f.seek(link)          
                
        # Passo 4
        print "Compressing..."

        with open( "temp", "rb") as f:
            type = 2#compressions[name]
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
    parser.add_argument( '-s1', dest = "src1", type = str, nargs = "?", default = "" )
    parser.add_argument( '-d', dest = "dst", type = str, nargs = "?", required = True )
    
    args = parser.parse_args()
    
    # dump bg
    if args.mode == "e0":
        print "Unpacking background"
        unpackBackground( args.src, args.src1, args.dst )
    # insert bg
    elif args.mode == "i0": 
        print "Packing background"
        packBackground( args.src, args.src1, args.dst )
    # dump ani
    elif args.mode == "e1": 
        print "Unpacking animation"
        unpackSprite( args.src, args.src1 , args.dst )
    # insert ani
    elif args.mode == "i1": 
        print "Packing animation"
        print args.src1
        packSprite( args.src , args.src1 , args.dst )
    else:
        sys.exit(1)
