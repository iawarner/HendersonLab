#!/usr/bin/python
## To call this script:
## python figure.py <start_no> <end_no>

## Import packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import sys
import os
import csv
import matplotlib as mpl
from collections import defaultdict


## Check inputs
print(sys.argv[1])
print(sys.argv[2])


'''
## Function to get gene colour
# This info can be derived from insertion index score table
essential_dict = defaultdict(dict)

def decide_colour():
    with open('BW_NTL_results_FD_SJ.csv', 'r') as f:
        reader = csv.DictReader(f)
        essential_inspect = list(reader)
    essential_inspect=np.array(essential_inspect)

    for line in essential_inspect:
        gene = line ["Gene"]
        essential = line ["essential"]

        essential_dict[gene]["essential"] = essential

    return essential_dict

decide_colour()

'''



## Function to draw figure
def make_fig (start,end):

    ## Read in data
    ## .csv file = variation of .gff file, with only CDS annotation information
    with open('CP009273.1.BW25113.CDS.csv', 'r') as f:
        reader = csv.reader(f)
        CDSinspect = list(reader)
    CDSinspect=np.array(CDSinspect)

   
    ## insertion data
    insertions_above = np.genfromtxt("testpos_1.txt", delimiter='\n', dtype=["int_"])
    insertions_below = np.genfromtxt("testneg_m1.txt", delimiter='\n', dtype=["int_"])

    ## Plot insertions above/below centre track - outgrowth
    plt.stem(range(int(start)+1,int(end)+1), insertions_above[int(start):int(end)], linefmt='grey', markerfmt=' ', basefmt='k')
    plt.stem(range(int(start)+1,int(end)+1), insertions_below[int(start):int(end)], linefmt='deeppink', markerfmt=' ', basefmt='k')


    ## Define axis
    #plt.xticks([])
    plt.yticks([])

    ## X axis start and end - taken from command input
    xs = int(start)
    xe = int(end)

    ax = plt.axes()
    ax.set_xlim(xs, xe)
    ax.set_ylim(-5, 5)
    
    ## Add genes to plot
    for line in CDSinspect:
        
        if int(start) or int(end) < int(line[3]) and int(line[3]) < int(end):

            ## Use this section to manually define CDS colour
            ## arrow_colour = 'chartreuse'          # for essential
            ## arrow_colouw = 'silver'              # for NE
            arrow_colour = 'silver'

            ## Get gene name
            label = str(line[8])
            label_elements = label.split(";")
            
            label_dictionary = {}
            
            #Go through each element in the label list, split it by the equals sign (values[0] will be on the left, values[1] on the right)
            for element in label_elements:
                values = element.split("=")

                #Create an entry in the dict, using the left side as the key, and the right side as the value
                label_dictionary[values[0]] = values[1]
            
            gene_name = label_dictionary["gene"]

            '''
            ## Get the gene colour from essential data
            gene_essentiality = str(essential_dict[gene_name]["essential"])

            
            if gene_essentiality == "TRUE":
                arrow_colour ='chartreuse'
            else:
                arrow_colour ='silver'
            
            '''

            '''
            ### Colour a specific CDS using exact coordinate match
            if int(line[3]) == 3971961:
                arrow_colour ='darkgrey'
            else:
                arrow_colour ='silver'
            '''


            ## Plot Genes
            if line[6] == '+':
                x = int(line[3])
                y = int(line[4])
            
                #ax.text((x+((y-x)/2)-130), -0.1, '%s' % gene_name, style='italic')
                ax.arrow(x, 0, (y-x)+1, 0, width=0.5, length_includes_head='TRUE', fc=arrow_colour, ec='k', head_width=0.7, head_length=50, zorder=3)

            elif line[6] == '-':
                x = int(line[4])
                y = int(line[3])

                #ax.text((x+((y-x)/2)-50), -0.1, '%s' % gene_name, style='italic')
                ax.arrow(x, 0, (y-x)+1, 0, width=0.5, length_includes_head='TRUE', fc=arrow_colour, ec='k', head_width=0.7, head_length=50, zorder=3)
        

        ## Add scale bar
        ## single track position
        #bar_size = 200
        #ax.add_patch(patches.Rectangle(((xs+25), -0.75), bar_size, 0.05, fc='k'))
        #ax.text((xs+(bar_size/2)+50), -1.2, '%s' % bar_size+' bp', size='12')

        ## dual track position
        #bar_size = 100
        #ax.add_patch(patches.Rectangle(((xs+20), -1.5), bar_size, 0.05, fc='k'))
        #ax.text((xs+(bar_size/2)+200), -2, '%s' % bar_size+' bp', size='12')


    ## Add additional genes/annotations in this section 
    #ax.text(3342691+((576/2)-80), -0.1, '%s' % "yrbK", style='italic')
    #ax.arrow(3336195, 0, 576, 0, width=0.5, length_includes_head='TRUE', fc='chartreuse', ec='k', head_width=0.7, head_length=50, zorder=2)


    plt.show()

make_fig(sys.argv[1], sys.argv[2])





