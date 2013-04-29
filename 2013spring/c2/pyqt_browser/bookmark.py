#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:amd_yen.20130429214002.3979: * @file bookmark.py
#@@first


#############################################################################
## Copyright 2009 0xLab  
## Authored by Erin Yueh <erinyueh@gmail.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##
#############################################################################





#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429214002.3980: ** <<declarations>> (bookmark)
import sqlite3
#@-<<declarations>>
#@+others
#@+node:amd_yen.20130429214002.3981: ** connect
def connect():
        try:
            db = sqlite3.connect('bookmark.db')
            db.execute("CREATE TABLE IF NOT EXISTS bookmark(title text, url text)")
            db.commit()
        except IOError:
            print("cannot connect DB")
            db = None
        return db
#@+node:amd_yen.20130429214002.3982: ** read
def read(db):
        booklist = []
        booklist = db.execute("select title,url from bookmark").fetchall()
        #print booklist
        return booklist
#@+node:amd_yen.20130429214002.3983: ** add
def add(db,data):
        #print data
        db.execute("INSERT INTO bookmark(title, url) VALUES(?,?)",data)
        db.commit()
#@+node:amd_yen.20130429214002.3984: ** delete
def delete(db,data):
        if data.has_key('title') and data.has_key('url'):
            db.execute("delete from bookmark where title=:title and url=:url",data)
            db.commit()
#@+node:amd_yen.20130429214002.3985: ** refresh
def refresh(db):
         booklist = db.execute("select title,url from bookmark").fetchall()
         return booklist
#@+node:amd_yen.20130429214002.3986: ** close
def close(db):
        db.close()
#@-others
#@-leo
