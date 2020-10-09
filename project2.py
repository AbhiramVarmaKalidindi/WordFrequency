#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:35:09 2020

@author: abhiram
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class frequency():
    """
    Parameters
    ----------
    file_name : str, optional
        DESCRIPTION. The default is "text.txt".
    punc : str, optional
        DESCRIPTION. The default is ".,;:\"\'-_1234567890".

    Returns
    -------
    None.
    """
    def __init__(self,file_name="text.txt",punc=".,;:\"\'-_1234567890"):
       
        self.file_name=file_name
        self.punc=punc
        self.counter={}
        self.lines=[]
        
    def inp(self):
        file=open(self.file_name)
        self.lines=file.read()+"\n"
        self.lines=self.lines.replace("\n"," ")
        
    def count(self):
        """
        DESCRIPTION. Counts frequency of words irrespective of upper case, lower 
        case and 'punc' and stores in counter

        Returns
        -------
        None.

        """
        self.inp()
        word=""
        for i in self.lines:
            i.rstrip()
            if i != " " :
                word+=i
            
            else:
                if len(word)>0:
                    if word[-1] in self.punc:
                        word=word[:-1]
                    word=word.lower()
                    
            
                    if word in self.counter.keys():
                        self.counter[word]=self.counter[word]+1
                    else:
                        self.counter[word]=1
                    word=""
    def top_words(self,num=10):
        """
        
        
        Parameters
        ----------
        num : int, optional
            DESCRIPTION. The default is 10.

        Returns
        -------
        Dictionary of top ten words used.
        Output format:{word_freq:[word1,word2,....]}

        """
        st={}
        count=dict(sorted(self.counter.items(), key=lambda x: x[1], reverse=True))
        same_count=[]
        present_count = list(count.values())[0]
        broke=False
        iter=0
        for loop in count:
            if count[loop]==present_count:
                same_count.append(loop)
            else:
                st[present_count]=same_count
                present_count=count[loop]
                same_count=[loop]
                iter+=1
            if iter==num:
                broke=True
                break
        if broke==False:
            st[present_count]=same_count
        return(st)
        
    def pretty(self,my_dict):
        """
        

        Parameters
        ----------
        my_dict : dict

        Prints
        -------
        Keys and values of my_dict in redable format

        """
        temp=0
        for i in my_dict:
            temp+=1
            print("{}) {} -> {}".format(temp,i,', '.join(my_dict[i])))
            
    
    def word_cloud(self,stopwords={}):
        """
        

        Parameters
        ----------
        stopwords : set of strings, optional
            DESCRIPTION. The default is {}.

        Returns
        -------
        Word Cloud

        """
        wc=WordCloud(background_color="white",stopwords=stopwords)   
        wc.generate(self.lines)
        
        plt.figure(figsize = (8, 8), facecolor = None) 
        plt.imshow(wc) 
        plt.axis("off") 
        plt.tight_layout(pad = 0) 
  
        plt.show() 
        
text1=frequency()
text1.count()
res=text1.top_words(num=10)
text1.pretty(res)
text1.word_cloud()













