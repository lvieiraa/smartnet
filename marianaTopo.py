import pdb
from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):
        
        Topo.__init__( self )

        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )
        s9 = self.addSwitch( 's9' )
        s10 = self.addSwitch( 's10' )
        s11 = self.addSwitch( 's11' )
        s12 = self.addSwitch( 's12' )
        s13 = self.addSwitch( 's13' )
        s14 = self.addSwitch( 's14' )
        s15 = self.addSwitch( 's15' )
        s16 = self.addSwitch( 's16' )
        s17 = self.addSwitch( 's17' )
        s18 = self.addSwitch( 's18' )
        s19 = self.addSwitch( 's19' )
        s20 = self.addSwitch( 's20' )
        s21 = self.addSwitch( 's21' )       
     
 
   

        self.addLink( s1, s3 ) #L 1,3
        self.addLink( s2, s19 ) #L 2,9,10,33,34,31,32
        self.addLink( s2, s20 ) #L 2,5,7,(8.1),23,24,25,26,30,31,34,36
        self.addLink( s4, s8 ) #L 4,9,10,11
        self.addLink( s17, s8 ) #L 27,25,24,23,14,17,18,29,34,33,11 
        self.addLink( s21, s8 ) #L 35,33,11
        self.addLink( s2, s19 ) #L 2,9,10,33,34,31,32
        self.addLink( s2, s20 ) #L 2,5,7,(8.1),23,24,25,26,30,31,34,36
        self.addLink( s4, s8 ) #L 4,9,10,11
        self.addLink( s5, s8 ) #L 27,25,24,23,14,17,18,29,34,33,11
	self.addLink( s6, s18 ) #L 8,7,5,9,10,33,34,31,30,28  
	self.addLink( s7, s5 ) #L (9.1),9,5,5
	self.addLink( s8, s16 ) #L 11,33,34,31,30,26,25  
	self.addLink( s9, s15 ) #L 12,14,17,18,20,21   
	self.addLink( s10, s5 ) #L 13,(8.1),7,6 
	self.addLink( s11, s8 ) #L 17,18,29,34,33,11 
	self.addLink( s12, s19 ) #L 16,17,14,23,24,25,26,30,32 
	self.addLink( s13, s5 ) #L 19,18,17,14,(8.1),7,6 
	self.addLink( s14, s21 ) #L 22,20,29,34,35   
	self.addLink( s15, s5 ) #L 21,20,18,17,14,(8.1),7,6
	self.addLink( s16, s19 ) #L 25,26,30,32  
	self.addLink( s17, s20 ) #L 27,26,30,31,34,35 
	self.addLink( s18, s8 ) #L 26,25,24,23,14,17,18,29,34,33,11 
	self.addLink( s19, s5 ) #L 32,30,26,25,24,23,(8.1),7,6  
	self.addLink( s20, s5 ) #L 36,34,29,18,17,14,(8.1),7,6 
	self.addLink( s21, s8 ) #L 35,33,11 
	self.addLink( s21, s18 ) #L 35,34,31,30,28 
	self.addLink( s5, s1 ) #L 6,5,1  
	self.addLink( s12, s20 ) #L 16,18,29,34,36 
	self.addLink( s18, s5 ) #L 28,30,31,29,18,17,14,(8.1),7,6 
	self.addLink( s13, s10 ) #L 19,18,17,14,13 
	self.addLink( s3, s5 ) #L 3,5,6 
	self.addLink( s14, s9 ) #L 22,20,18,17,14,12  
	self.addLink( s18, s9 ) #L 26,25,24,23,13,12 
	self.addLink( s7, s21 ) #L (9.1),9,5,7,(8.1),23,24,25,26,30,34,35  
	 
  


topos = { 'mytopo': ( lambda: MyTopo() ) }
