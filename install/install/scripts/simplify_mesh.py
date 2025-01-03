#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

""" @package dataset_tools_preprocess
This script calls meshlab to simplify a mesh

Parameters: -h help,
            -inputMesh <the mesh to simplify>,
            -outputMesh <the output mesh>,
            -meshlabPath <Meshlab binary directory>

Usage: python simplify_mesh.py --inputMesh <the mesh to simplify>
                               --outputMesh <the output mesh>
                               --meshlabPath <Meshlab binary directory>
                               --meshsize <size of the output mesh in K polygons (ie 200 == 200,000 polygons). Values allowed: 200, 250, 300, 350, 400>

"""

import os, sys
import argparse
from utils.commands import runCommand
from utils.paths import getMeshlabPath

def simplifyMesh(inputMesh, outputMesh, meshsize="", meshlabPath = getMeshlabPath(), meshlabServerExe = 'meshlabserver.exe'):
    mlxFileEnd = 'meshlab/simplify.mlx'

    if( meshsize != "" ):
        if( meshsize == "200"):
            mlxFileEnd = 'meshlab/simplify200.mlx'
        elif( meshsize == "250"):
            mlxFileEnd = 'meshlab/simplify250.mlx'
        elif( meshsize == "300"):
            mlxFileEnd = 'meshlab/simplify300.mlx'
        elif( meshsize == "350"):
            mlxFileEnd = 'meshlab/simplify350.mlx'
        elif( meshsize == "400"):
            mlxFileEnd = 'meshlab/simplify400.mlx'


    mlxFile = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), mlxFileEnd))

    return runCommand(os.path.abspath(os.path.join(meshlabPath, meshlabServerExe)), ['-i', inputMesh,
                                                                              '-o', outputMesh,
                                                                              '-s', mlxFile])

def main():
    parser = argparse.ArgumentParser()

    meshlabPath = os.environ['MESHLAB_PATH'] if 'MESHLAB_PATH' in os.environ else "C:\\Program Files\\VCG\\Meshlab"

    # common arguments
    parser.add_argument("--inputMesh", type=str, required=True, help="the mesh to simplify")
    parser.add_argument("--outputMesh", type=str, required=True, help="the output mesh")
    parser.add_argument("--meshlabPath", type=str, default=getMeshlabPath(), help="Meshlab binary directory")
    parser.add_argument("--meshsize", type=str, help="size of the output mesh in K polygons (ie 200 == 200,000 polygons). Values allowed: 200, 250, 300, 350, 400")

    args = vars(parser.parse_args())

    return simplifyMesh(args['inputMesh'], args['outputMesh'], args['meshsize'], args['meshlabPath'])

#    sys.exit(0)

if __name__ == "__main__":
    main()
