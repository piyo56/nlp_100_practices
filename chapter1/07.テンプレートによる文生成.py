#set fileencdoing=utf-8
"""
07. $B%F%s%W%l!<%H$K$h$kJ8@8@.(B
$B0z?t(Bx, y, z$B$r<u$1<h$j!V(Bx$B;~$N(By$B$O(Bz$B!W$H$$$&J8;zNs$rJV$94X?t$r<BAu$;$h!%$5$i$K!$(Bx=12, y="$B5$29(B", z=22.4$B$H$7$F!$<B9T7k2L$r3NG'$;$h!%(B
"""
def mkStr(x,y,z):
    #return str(x)+"$B;~$N(B"+str(y)+"$B$O(B"+str(z)
    return "{0}$B;~$N(B{1}$B$O(B{2}".format(x,y,z)
    #return "{x}$B;~$N(B{y}$B$O(B{z}".format(**locals())
if __name__=="__main__":
   print ( mkStr(12,"$B5$29(B",22.4) )
