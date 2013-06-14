
#coding: utf-8
#Simple CAD Programm  !! prototyp !!
#
#Copyright (C) 2010 Micha Rethfelder micha.rathfelder@gmail.com
#
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/>.
#

from tkinter import *
import math
class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.header = Frame()
        self.header.pack(side="top",expand=1,fill="x")
        
        

        self.center = Frame()
        self.center.pack(side="top",expand=1,fill="both")

        self.footer = Frame()
        self.footer.pack(side="bottom",expand=1,fill="x")

        self.mid = Frame(master=self.center)
        self.mid.pack(side="left",expand=1,fill="both")

        self.tool = Frame(master=self.center)
        self.tool.pack(side="left",expand=1,fill="x")
        
        self.listbox = Listbox(master=self.tool)
        self.listbox.pack(side="top",expand=1,fill="both")

        self.editor = Text(master=self.tool,width=22,height=20)
        self.editor.pack(side="bottom",expand=1,fill="y")

        # --- HEADER ---
        
        cfg = {}
        cfg["text"] = "Circle畫圓"
        cfg["fg"]   = "black"
        cfg["command"] =  self.draw_kreis
        Button(self.header,cfg).pack(side= "left")

        cfg = {}
        cfg["text"] = "Line畫線"
        cfg["fg"]   = "black"
        cfg["command"] =  self.draw_line
        Button(self.header,cfg).pack(side= "left")

        cfg = {}
        cfg["text"] = "Point畫點"
        cfg["fg"]   = "black"
        cfg["command"] = self.draw_point
        Button(self.header,cfg).pack(side= "left")

        cfg = {}
        cfg["text"] = "Autofang"
        cfg["fg"]   = "black"
        cfg["command"] = self.autofang
        self.button_autofang = Button(self.header,cfg).pack(side= "left")

        # --- PAPER ---
        self.paper = Canvas(master=self.mid)
        self.paper["bg"] = "black"
        self.paper["width"] = 500
        self.paper["height"] = 500
        self.paper.pack(side="left",expand=1,fill="both")
        self.last_x = 0
        self.last_y = 0
        self.paper.create_text(10,5,text=self.last_x,fill="green",tag="pos_x", anchor="nw")
        self.paper.create_text(10,20,text=self.last_x,fill="green",tag="pos_y", anchor="nw")
        self.paper.create_text(10,60,text="Tool:",fill="yellow",tag="tool", anchor="nw")
        self.paper.create_text(10,80,text="Schritt:",fill="yellow",tag="step", anchor="nw")


        self.paper.create_rectangle(0,0,0,0,tag="near",outline="darkblue")
        self.paper.create_rectangle(0,0,0,0,tag="near1",outline="yellow")
        self.paper.create_rectangle(0,0,0,0,tag="near2",outline="yellow")
        self.paper.create_rectangle(0,0,0,0,tag="near3",outline="yellow")
        self.paper.create_rectangle(0,0,0,0,tag="near4",outline="yellow")
        self.paper.create_rectangle(0,0,0,0,tag="near5",outline="yellow")
        self.paper.bind("<Motion>",self.pointer)
        self.paper.bind("<ButtonPress-1>",self.action)
        #self.paper.bind("<Motion>",self.move)
        self.paper.bind("<ButtonPress-3>",self.button2_press)
        self.paper.bind("<ButtonRelease-3>",self.button2_release)
        # --- FOOTER ---
        Label(self.footer,text="command:").pack(side= "left")
        self.Entry = Entry(self.footer)
        self.Entry.pack(side= "left",expand=1 ,fill="x")
        for i in dir(self.paper):
            if "item" in i:
                print (i)
    def move(self,event):
        if self.button2 :
           print (event.x ,event.y)

    def button2_press(self,event=None):
        self.button2 = 1
        self.paper.yview_moveto(+100)
    def button2_release(self,event=None):
        self.button2 = 0   
        self.paper.yview_moveto(+100)     
    def kreis_mitelpunkt_radius(self,event=None):
        diff_x = self.centre[0]- event.x
        diff_y = self.centre[1]- event.y

        hyp = int(math.sqrt( diff_y**2 + diff_x**2 ))
        coords = (self.centre[0]-hyp  , self.centre[1]-hyp  , self.centre[0]+hyp, self.centre[1]+hyp  )
        #print coords
        self.paper.coords('curent', coords)      

    def linie(self,event=None):

        coords = (self.centre[0]  , self.centre[1]  , event.x, event.y  )
        print (coords)
        self.paper.coords('curent', coords)      
    
    def point(self,event=None):

        coords = self.centre #[0]  , self.centre[1]  , event.x, event.y  )
        print (coords)
        self.paper.coords('curent', coords)      

    def pointer(self,event):
        self.paper.itemconfigure('pos_x', text="x=%0.3f" % event.x )
        self.paper.itemconfigure('pos_y', text="y=%0.3f" % event.y)

        self.paper.coords('near', 0,0,0,0)
        self.paper.coords('near1', 0,0,0,0)
        self.paper.coords('near2', 0,0,0,0)
        self.paper.coords('near3', 0,0,0,0)
        self.paper.coords('near4', 0,0,0,0)
        self.paper.coords('near5', 0,0,0,0)
        if self.tool == "kreis" and self.step == 1:
            self.kreis_mitelpunkt_radius(event)
        if self.tool == "linie" and self.step == 1:
            self.linie(event)
  
        else:
            closest = self.paper.find_closest(event.x, event.y)
            
            tags    = self.paper.gettags(closest) 

            if "drawing" in tags:
                self.closest = closest
           
                #print closest
                #print tags
                #print self.paper.bbox(self.closest)
                #print self.closest
                coords = self.paper.coords(self.closest)
                #print dir(self.paper)
                
                self.listbox.delete(0,"end")
                for  i in self.paper.find_all():
                    if "drawing" in self.paper.gettags(i):
                        self.listbox.insert("end","item %i %s %s" % (i,self.paper.type(i),str(self.paper.gettags(i)) ) )
                self.editor.delete(0.0,"end")
                (x1, y1, x2, y2) = self.paper.coords(self.closest)
                x_mitte = (x1+x2)/2
                y_mitte = (y1+y2)/2
                self.editor.insert("end", "x1,y1="+str(self.paper.coords(self.closest)[:2])+"\n")
                self.editor.insert("end", "x2,y2="+str(self.paper.coords(self.closest)[2:])+"\n")
                self.editor.insert("end", "l\xc3\xa4nge=%0.2f\n" % math.sqrt((x1-x2)**2+(y1-y2)**2) )
                self.editor.insert("end", str(self.paper.type(self.closest))+"\n")
                self.editor.insert("end", str(self.paper.gettags(self.closest))+"\n")                

                (x1, y1, x2, y2) = coords
                x_mitte = (x1+x2)/2
                y_mitte = (y1+y2)/2
        

                #self.editor.insert("end", str(x_pn)+ " "+ str(min_y) +"\n")                


                if "line" == self.paper.type(self.closest):
                    self.paper.coords('near1', (x1-4,y1-4,x1+4,y1+4) )   
                    self.paper.coords('near2', (x2-4,y2-4,x2+4,y2+4) )
                  
                    self.paper.coords('near3', (x_mitte-4,y_mitte-4,x_mitte+4,y_mitte+4) )

                if "oval" == self.paper.type(self.closest):
                    self.paper.coords('near1', ( x_mitte-4, y_mitte-4, x_mitte+4 , y_mitte+4 ) ) 

                    self.paper.coords('near2', ( x1-4, y_mitte-4, x1+4 , y_mitte+4 ) ) 
                    self.paper.coords('near3', ( x2-4, y_mitte-4, x2+4 , y_mitte+4 ) ) 
                    self.paper.coords('near4', ( x_mitte-4, y1-4, x_mitte+4 , y1+4 ) ) 
                    self.paper.coords('near5', ( x_mitte-4, y2-4, x_mitte+4 , y2+4 ) ) 

                    
         

                self.paper.coords('near', (coords[0]-1,coords[1]-1,coords[2]+1,coords[3]+1) )          
        self.move(event)
    def draw_kreis(self):
        self.tool = "kreis"
        self.step = 0
        self.paper.itemconfigure('tool', text="Tool:\t%s" % self.tool )
        self.paper.itemconfigure('step', text="Schritt:\t%i" % self.step )

    def draw_line(self):
        self.tool = "linie"
        self.step = 0
        self.paper.itemconfigure('tool', text="Tool:\t%s" % self.tool )
        self.paper.itemconfigure('step', text="Schritt:\t%i" % self.step )

    def draw_point(self):
        self.tool = "point"
        self.step = 0
        self.paper.itemconfigure('tool', text="Tool:\t%s" % self.tool )
        self.paper.itemconfigure('step', text="Schritt:\t%i" % self.step )
    def autofang(self,event=None):
        print (dir( ))
        if self.autofang_m1 == 0:
           #self.button_autofang["fg"] = "green" 
           self.autofang_m1 = 1
        else:
           pass
           #self.button_autofang["fg"] = "black" 
    def action(self,event=None):

        print ("hi",event.x,event.y)
        if self.tool == "kreis":
            if self.step == 0:
                self.paper.create_oval(event.x, event.y, event.x, event.y,  outline="yellow", tag="curent")#,style="arc")
                self.centre = (event.x,event.y)
                print ("gezeichnent ",event.x,event.y)
                self.step = 1                            
            elif self.step == 1:
                self.paper.itemconfigure('curent', outline="green",tags="drawing" )

                self.step = 0
                self.tool = ""
        elif self.tool == "linie":
            if self.step == 0:
                self.paper.create_line(event.x, event.y, event.x, event.y,  fill="yellow", tag="curent")#,style="arc")
                self.centre = (event.x,event.y)
                print ("gezeichnent ",event.x,event.y)
                self.step = 1                            
            elif self.step == 1:
                self.paper.itemconfigure('curent', fill="green",tags="drawing" )

                self.step = 0
                self.tool = ""
        elif self.tool == "point":
            if self.step == 0:
                self.paper.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="green", outline="green", tag="drawing")#,style="arc")
                self.centre = (event.x,event.y)
                print ("gezeichnent ",event.x,event.y)
                self.step = 0 
                self.tool = ""                           
        self.paper.itemconfigure('tool', text="Tool:\t%s" % self.tool )
        self.paper.itemconfigure('step', text="Schritt:\t%i" % self.step )                                    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.button2 = 0   
        self.autofang_m1 = 0  
   
print ("make frame")
root = Tk()
root.title("簡單的 CAD 程式")
print ("app started")
app = Application(master=root)
print ("mainloop started")
app.mainloop()
print ("mainloop ended")

