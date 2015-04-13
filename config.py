#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#~ Copyright (C) 2014 Carlos Manuel Ferras Hernandez <c4rlos.ferra5@gmail.com>
#~ This file is part of Sequence-ToolKit.

#~ Sequence-ToolKit is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ Sequence-ToolKit is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with Sequence-ToolKit.  If not, see <http://www.gnu.org/licenses/>.

import commands
import os
import pickle

class config:
	
	def __init__(self):
		self.win=False
		try:
			a=str(commands.getoutput('$HOME'))
			b=a.split('/')
			del b[0]
			c=b[-1].split()
			del b[-1]
			if len(c)>1:
				d=c[0].split(':')
				e=d[0]
			else:
				e=c[0]
			self.userRoot=''
			for i in b:
				self.userRoot+='/'+i
			self.userRoot+='/'+e
			self.dir=self.userRoot+'/'
		except:
			self.win=True
		if not self.win:
			self.generalconf=self.dir+'.stk.conf'
			self.gensecconf=self.dir+'.genSec.conf'
			self.genrepconf=self.dir+'.genRep.conf'
		else:
			self.generalconf='stk.conf'
			self.gensecconf='genSec.conf'
			self.genrepconf='genRep.conf'
			
	
	def loadGeneral(self):
		config=['Novason',12,'',1,'','default']
		if os.path.exists(self.generalconf):
			file=open(self.generalconf,'r')
			try:
				while True:
					line =file.readline()
					if not line:
						break
					if not line.find('Font '):
						config[0]=str(line.split("[")[1].split("]")[0])
					elif not line.find('Size '):
						try:
							config[1]=int(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('File Location '):
						config[2] =str(line.split("[")[1].split("]")[0])
					elif not line.find('Opacity '):
						try:
							config[3]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Lang '):
						config[4] =str(line.split("[")[1].split("]")[0])
					elif not line.find('Theme '):
						config[5] =str(line.split("[")[1].split("]")[0])
			except:
				pass
			file.close()
		return config
	
	
	def saveGeneral(self,fuente,size,fileLocation,opacity,lang,theme):
		file=open(self.generalconf,'w+').close()
		file=open(self.generalconf,'w+')
		file.write("Font ["+str(fuente)+"]\n"+"Size ["+str(size)+"]\n"+"File Location ["+str(fileLocation)+"]\n"+"Opacity ["+str(opacity)+"]\n"+"Lang ["+str(lang)+"]\n"+"Theme ["+str(theme)+"]\n")
		file.close()
		return True
		
		
	def loadGenSec(self):
		config=['#6695df','#4e72aa','#8665df',[False,False,False,False,False,False,False,[False,False],False]]
		if os.path.exists(self.gensecconf):
			file=open(self.gensecconf,'r')
			try:
				while True:
					line =file.readline()
					if not line:
						break
					if not line.find('Color1 '):
						config[0] =str(line.split("[")[1].split("]")[0])
					elif not line.find('Color2 '):
						config[1] =str(line.split("[")[1].split("]")[0])
					elif not line.find('Color3 '):
						config[2] =str(line.split("[")[1].split("]")[0])
					elif not line.find('Defaults Process'):
						config[3] =pickle.load(file)
						if config[3] ==[]:
							config[3] =[False,False,False,False,False,False,False,[False,False],False]
			except:
				pass
			file.close()
		return config
	
	
	def saveGenSec(self,col1,col2,col3,processDefaults):
		file=open(self.gensecconf,'w+').close()
		file=open(self.gensecconf,'w+')
		file.write("Color1 ["+str(col1)+"]\n"+"Color2 ["+str(col2)+"]\n"+"Color3 ["+str(col3)+"]\n"+"Defaults Process\n")
		pickle.dump(processDefaults,file)
		file.close()
		return True
		
	
	def loadGenRep(self):
		config=[[1],0,'linear',-1,-1,20,5,0,'lineal',-1,-1,5000,500,1,1,0,10,-10,0,True,[]]
		if os.path.exists(self.genrepconf):
			file=open(self.genrepconf,'r')
			try:
				while True:
					line =file.readline()
					if not line:
						break
					if not line.find('Curve to show '):
						try:
							temp=str(line.split("[")[1].split("]")[0])
							ints=[int(i) for i in temp.split(',')]
							if ints[0]!='':
								config[0]=ints
						except:
							pass
					elif not line.find('Show TL '):
						try:
							config[1]=int(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Horizontal Scale '):
						config[2]=str(line.split("[")[1].split("]")[0])
					elif not line.find('Horizontal Minimum '):
						try:
							config[3]=float(line.split("[")[1].split("]")[0])
						except:
							pass	
					elif not line.find('Horizontal Maximum '):
						try:
							config[4]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Horizontal Greater Unity '):
						try:
							config[5]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Horizontal Smallest Unity '):
						try:
							config[6]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Unit '):
						try:
							config[7]=int(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Vertical Scale '):
						config[8]=str(line.split("[")[1].split("]")[0])
					elif not line.find('Vertical Minimum '):
						try:
							config[9]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Vertical Maximum '):
						try:
							config[10]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Vertical Greater Unity '):
						try:
							config[11]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find('Vertical Smallest Unity '):
						try:
							config[12]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					
					elif not line.find("Signal "):
						try:
							config[13]=int(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find("Background "):
						try:
							config[14]=int(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find("Low Signal "):
						try:
							config[15]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find("High Signal "):
						try:
							config[16]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find("Low Background "):
						try:
							config[17]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find("High Background "):
						try:
							config[18]=float(line.split("[")[1].split("]")[0])
						except:
							pass
					elif not line.find("Consecutives "):
						try:
							config[19]=bool(int(line.split("[")[1].split("]")[0]))
						except:
							pass
					elif not line.find('Parameters '):
						try:
							temp=str(line.split("[")[1].split("]")[0])
							ints=[int(i) for i in temp.split(',')]
							if ints[0]!='':
								config[20]=ints
						except:
							pass
			except:
				pass
			file.close()
		return config
	
	
	def saveGenRep(self,curve_to_show,show_tl,h_scale,h_min,h_max,h_great_unit,h_small_unit,unit,v_scale,v_min,v_max,v_great_unit,v_small_unit,signal,background,s_low,s_high,b_low,b_high,consecutives,parameters):
		file=open(self.genrepconf,'w+').close()
		file=open(self.genrepconf,'w+')
		curve_to_show=str(curve_to_show)[1:-1]
		parameters=str(parameters)[1:-1]
		file.write("Curve to show ["+str(curve_to_show)+"]\n"+"Show TL ["+str(show_tl)+"]\n"+"Horizontal Scale ["+str(h_scale)+"]\n"+"Horizontal Minimum ["+str(h_min)+"]\n"+"Horizontal Maximum ["+str(h_max)+"]\n"+"Horizontal Greater Unity ["+str(h_great_unit)+"]\n"+"Horizontal Smallest Unity ["+str(h_small_unit)+"]\n"+"Unit ["+str(unit)+"]\n"+"Vertical Scale ["+str(v_scale)+"]\n"+"Vertical Minimum ["+str(v_min)+"]\n"+"Vertical Maximum ["+str(v_max)+"]\n"+"Vertical Greater Unity ["+str(v_great_unit)+"]\n"+"Vertical Smallest Unity ["+str(v_small_unit)+"]\n"+"Signal ["+str(signal)+"]\n"+"Background ["+str(background)+"]\n"+"Low Signal ["+str(s_low)+"]\n"+"High Signal ["+str(s_high)+"]\n"+"Low Background ["+str(b_low)+"]\n"+"High Background ["+str(b_high)+"]\n"+"Consecutives ["+str(int(consecutives))+"]\n"+"Parameters ["+str(parameters)+"]\n")
		file.close()
		return True
	
		
		
		
		
		
		
