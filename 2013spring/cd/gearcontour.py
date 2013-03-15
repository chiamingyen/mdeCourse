#coding: utf-8
'''正齒輪 2D 繪圖, 採用 Python3 tkinter 介面
'''
from tkinter import *
# 導入所有的數學函式
from math import *
# 導入數學函式後, 圓周率為 pi
# deg 為角度轉為徑度的轉換因子
deg = pi/180.
#
# 以下分別為正齒輪繪圖與主 tkinter 畫布繪圖
#
# 定義一個繪正齒輪的繪圖函式
# midx 為齒輪圓心 x 座標
# midy 為齒輪圓心 y 座標
# rp 為節圓半徑, n 為齒數
def gear(畫布, midx, midy, rp, n, 顏色):
#canvas.create_line(0, 300, 150, 150, width=10, fill='green')
    # 將角度轉換因子設為全域變數
    global deg
    # 齒輪漸開線分成 15 線段繪製
    imax = 15
    # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
    畫布.create_line(midx, midy, midx, midy-rp)
    # 畫出 rp 圓
    #畫布.create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
    # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
    # 模數也就是齒冠大小
    a=2*rp/n
    # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
    d=2.5*rp/n
    # ra 為齒輪的外圍半徑
    ra=rp+a
    # 畫出 ra 圓
    #畫布.create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
    # rb 則為齒輪的基圓半徑
    # 基圓為漸開線長齒之基準圓
    rb=rp*cos(20*deg)
    # 畫出 rb 圓 (基圓)
    #畫布.create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
    # rd 為齒根圓半徑
    rd=rp-d
    # 畫出 rd 圓 (齒根圓)
    #畫布.create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
    # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
    # 將圓弧分成 imax 段來繪製漸開線
    dr=(ra-rb)/imax
    # tan(20*deg)-20*deg 為漸開線函數
    sigma=pi/(2*n)+tan(20*deg)-20*deg
 
    for j in range(n):
        ang=-2.*j*pi/n+sigma
        ang2=2.*j*pi/n+sigma
        lxd=midx+rd*sin(ang2-2.*pi/n)
        lyd=midy-rd*cos(ang2-2.*pi/n)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(alpha-ang)
            ypt=r*cos(alpha-ang)
            xd=rd*sin(-ang)
            yd=rd*cos(-ang)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            畫布.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                lfx=midx+xpt
                lfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        '''
        the line from last end of dedendum point to the recent
        end of dedendum point
        '''
        # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
        # 下列為齒根圓上用來近似圓弧的直線
        畫布.create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=顏色)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(ang2-alpha)
            ypt=r*cos(ang2-alpha)
            xd=rd*sin(ang2)
            yd=rd*cos(ang2)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            畫布.create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                rfx=midx+xpt
                rfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
        # 下列為齒頂圓上用來近似圓弧的直線
        畫布.create_line(lfx,lfy,rfx,rfy,fill=顏色)
#
# 以下為 tkinter 畫布繪圖主內容
#
frame=Frame()
frame.master.title("正齒輪繪圖範例")
frame.pack()
 
canvas = Canvas(width=800, height=800, bg='white')
 
canvas.pack(expand=YES, fill=BOTH) 
gear(canvas,400,400,300,16,"blue")
#gear(canvas,400,400,100,36,"red")
#gear(canvas,400,400,200,36,"dark green")
'''
canvas.create_line(100, 100, 200, 200)             
canvas.create_line(100, 200, 200, 300)
'''
# 加入其他畫布繪圖
for i in range(1, 50, 4): 
    canvas.create_line(0, i, 50, i)
    canvas.create_line(i, 0, i, 50)
 
mainloop()
