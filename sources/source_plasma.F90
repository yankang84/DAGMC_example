!  RDUM(1): 1.0 for D-D plasma( mean nuetron energy 2.45 MeV) otherwise
!           D-T plasma assumed( mean neutron energy 14.1) 
!  RDUM(2): Temperature of plasma in KeV
!  RDUM(3): Plasma major radius (cm)
!  RDUM(4): Plasma minor radius (cm)
!  RDUM(5): Elongation
!  RDUM(6): Triangularity
!  RDUM(7): Plasma radial shift (cm)
!  RDUM(8): Plasma peaking factor
!  RDUM(9): Plasma vertical shift(cm)(+ = up)
!  RDUM(10): Start of angular extent (degrees)
!  RDUM(11): Range of angular extent (degrees)
!  (         Parameters rdum(10) and rdum(11) should be used if only a section of
!   the tokamak is modelled with reflecting planes at each end. The weight of 
!   the starting particles is adjusted accordingly. Set rdum(10) = 0 and 
!   rdum(11) = 360.0 if a full tokamak is modelled.)
!
!  1(1): number of valid cell numbers to follow
!  IDUM(2) to IDUM(IDUM(1)+1) = valid source cells

!new version for MCNP6
! AT modified to support idum(1) as selector.
!IDUM(1) = calls this subroutine. IDUM(2) = number of source cells to follow.
!IDUM(3 - ) = source cells.
!RDUMs are standard.
! THIS LINE CHANGED
!      DO I=1,IDUM(1)                                                    
!         pbl%i%icl = NAMCHG(1,IDUM(I+1)) 
! to
!      DO I=1,IDUM(2)                                                    
!         pbl%i%icl = NAMCHG(1,IDUM(I+2)) 


subroutine plasma
        ! dummy subroutine.  aborts job if source subroutine is missing.
  ! if nsr==USER_DEFINED_SOURCE, subroutine source must be furnished by the user.
  ! at entrance, a random set of uuu,vvv,www has been defined.  the
  ! following variables must be defined within the subroutine:
  ! xxx,yyy,zzz,icl,jsu,erg,wgt,tme and possibly ipt,uuu,vvv,www.
  ! subroutine srcdx may also be needed.

  ! .. Use Statements ..
  use mcnp_interfaces_mod, only : expirx
  use mcnp_debug
  use mcnp_global
  use mcnp_random
  use mcnp_params, only : DKND
  use pblcom, only : pbl
  use tskcom
  use mcnp_particles, only: neutron
    use varcom, only : dbcn, nps, ion_a, ion_z, ion_chg, ion_zaid,          &
    & ion_src_a, ion_src_z, ion_src_chg
  
  ! ZG@CCFE modified variables to match MCNP6 nomenclature


  implicit real(dknd) (a-h,o-z)
  character*60 string(100)  
  real TestErg                                       

   ! modified model for 360 degree, generalised source cell      
   ! problem                                                               
   !                                                                       
   !       integer order                                                   
   !                                                                       
   ! *** set type of particle (=1 for neutrons)                            
      pbl%i%ipt=1                                                             
   ! *** set cell number of source as that input in source card            
   !      icl=idum(1)                                                      
   ! *** set surface of departure (=0 if start point is not on a surface)  
      pbl%i%jsu=0                                                             
   ! *** set statistical weight                                            
      pbl%r%wgt=rdum(11)/360.0                                                
   ! *** set time of particle production                                   
      pbl%r%tme=0.0                                                           
   ! *** calculate energy of particle                                      
 100  t1=2.*rang()-1.                                                   
      t2=t1**2+rang()**2                                                
      if(t2.gt.1.0.or.t2.eq.0.0) goto 100                               
   ! *** set particle energy and ion temperature from data in rdum array   
   !      qq1=sqrt(rdum(1))                                                
      if(rdum(1).eq.1.0)then                                            
         qq1=sqrt(2.45)                                                 
         fudge = 1000.0                                                 
      else if(rdum(1).eq.2.0)then                                                              
         qq1=sqrt(14.1)                                                 
         fudge=1237.4                                                   
! ********** addition of the TT reaction ********************************************
      else if(rdum(1).eq.3.0)then
      ! The T+T case has three channels (Casey et al., 2012): 
      ! t+t -> (1) 4He + 2n; (2) 5He(GS) + n; (3) 5He(ES) + n
      ! These occur in different ratios, which are communicated via the  RDUM() variable
      ! channels (2) and (3) are triggered with RDUM(14) = 100, else only channel (1)
      ! ratio (1) = RDUM(15) ratio (2) = RDUM(16) ratio (3) = RDUM(17)        
      ! RDUM(18) defines, whether the decay of the 5He nucleus is treated
      
      !Randomly select the channel, by accounting for these weights
          t5=rang() !needed to select the channel
         
     ! executed if no individual channel ratios are entered - RDUM(14) = 0   
          if(rdum(14).ne.(100.0)) then  

     ! only the channel (1) reaction
             pbl%r%wgt=rdum(11)/360.0 * 2   ! determine weight of n per TT reaction 
             mu1= 4.72                       ! i.e. close to 2 neutrons / reaction
             s1 = 4.72 !An elliptical distribution (Matsuzaki et al., 2004, Fig. 3)
             phi= acos(t3) !Because of the condition for t4, this will give the correct 
             !distribution of angles phi.
             R=2.*rang()-1. 
             en1=mu1+s1*sin(phi)*R  !The half-circle is centred at mu1 with a radius of s1
             qq1=sqrt(en1)  ! comunicated energy (square root)
  
        ! executed if individual channel ratios are entered - triggered by RDUM(14)=100   
         else if(rdum(14).eq.(100.0)) then  
              if(rdum(18).eq.(0.0)) then  ! 5He decay not treated
                   pbl%r%wgt=rdum(11)/360.0*(2*rdum(15)+rdum(16)+rdum(17))&
                   &/(rdum(15)+rdum(16)+rdum(17))
                   t5=t5*(2*rdum(15)+rdum(16)+rdum(17))
                   if(t5.le.(2*rdum(15)) )then ! (1)
                           mu1= 4.72
                           s1 = 4.72 !An elliptical distribution (Matsuzaki et al., 2004, Fig. 3)
                           phi= acos(t3) 
                           R=2.*rang()-1.
                           en1=mu1+s1*sin(phi)*R
                           qq1=sqrt(en1)
                   else if(t5.gt.(2*rdum(15)).and.t5.le.(2*rdum(15)&
                   &+rdum(16)))then ! (2)
                           mu2= 8.778 !(Bogdanova et al., 2015, Eq. (10))
                           s2= 0.273  !(Bogdanova et al., 2015, Eq. (9))
                           en1 = mu2 + s2*t3*sqrt(-(2*log(t4))/t4)  ! Gaussian distribution energy of the neutron
                           !Energy is normally distributed around mu2 with a standard deviation of s2
                           qq1=sqrt(en1)
                   else if(t5.gt.(2*rdum(15)+rdum(16)))then ! (3)
                           mu3= 7.738 !(Bogdanova et al., 2015, Eqs. (8) & (11))
                           s3= 1.34  !(Bogdanova et al., 2015, Eq. (11))
                           en1 = mu3 + s3*t3*sqrt(-(2*log(t4))/t4)  ! Gaussian distribution energy of the neutron
                           qq1=sqrt(en1)
                   endif
               
              else if(rdum(18).eq.(1.0)) then  ! 5He decay also treated
                   pbl%r%wgt=rdum(11)/360.0 * 2
                   t5=t5*2*(rdum(15)+rdum(16)+rdum(17))
                   if(t5.le.(2*rdum(15)) )then ! (1)
                           mu1= 4.72
                           s1 = 4.72 !An elliptical distribution (Matsuzaki et al., 2004, Fig. 3)
                           phi= acos(t3) 
                           R=2.*rang()-1. 
                           en1=mu1+s1*sin(phi)*R !The half-circle is centred at mu1 with a radius of s1
                           qq1=sqrt(en1)
                   else if(t5.gt.(2*rdum(15)).and.t5.le.(2*rdum(15)&
                   &+rdum(16)))then ! (2)
                           mu2= 8.778 !(Bogdanova et al., 2015, Eq. (10))
                           s2= 0.273  !(Bogdanova et al., 2015, Eq. (9))
                           en1 = mu2 + s2*t3*sqrt(-(2*log(t4))/t4)  ! Gaussian distribution energy of the neutron
                           qq1=sqrt(en1)
                  else if(t5.gt.(2*rdum(15)+rdum(16)).and.t5.le.&
                  &(2*rdum(15)+rdum(16)+rdum(17))) then  ! (3)  
                           mu3= 7.738 !(Bogdanova et al., 2015, Eqs. (8) & (11))
                           s3= 1.34  !(Bogdanova et al., 2015, Eq. (11))
                           en1 = mu3 + s3*t3*sqrt(-(2*log(t4))/t4)  ! Gaussian distribution energy of the neutron
                           qq1=sqrt(en1)
                  else if(t5.gt.(2*rdum(15)+rdum(16)+rdum(17)).and&
                  &.t5.le.(2*rdum(15)+2*rdum(16)+rdum(17))) then  ! (2) - secondary)
                           mu2= 8.778 !(Bogdanova et al., 2015, Eq. (10))
                           s2= 0.273  !(Bogdanova et al., 2015, Eq. (9))
                           En2 = mu2 + s2*t3*sqrt(-(2*log(t4))/t4)  ! Gaussian distribution energy of the 1st neutron
                           EHe = 10.534 - (mu2 + s2*t3*&
                           &sqrt(-(2*log(t4))/t4)) ! Sqrt of Gaussian distribution energy of 5He
                           En0 = 0.6384                ! neutron energy due to 5He decay in CMS
                           en1 = EHe/4 + En0 + sqrt(EHe/4*En0)*& !(Bogdanova et al., 2015, Eq. (14)) 
                           &(2*rang()-1)                 ! Vector summation of 5He and neutron CMS velocities
                           qq1=sqrt(en1)
                  else if(t5.gt.(2*rdum(15)+2*rdum(16)+rdum(17)))then ! (3) - secondary
                           mu3= 7.738 !(Bogdanova et al., 2015, Eqs. (8) & (11))
                           s3= 1.34  !(Bogdanova et al., 2015, Eq. (11))
                           EHe = abs(9.264 - (mu3 + s3*t3*&
                           &sqrt(-(2*log(t4))/t4)))  ! Sqrt of Gaussian distribution energy of 5He
                           En0 = 1.6544                ! neutron energy due to 5He decay in CMS
                           en1 = abs(EHe/4 + En0 + &   !(Bogdanova et al., 2015, Eq. (14)) 
                           &sqrt(EHe/4*En0)*(2*rang()-1)) 
                           qq1=sqrt(en1)
                  endif
 
              endif     

           endif
           fudge = 1000.0
	   ! Absolute upper bound for neutron energy 9.443 MeV, smooth ending
	   !Moved inside of loop
           if((qq1**2-9.0).gt.(rang()*0.443)) goto 100
	   TestErg = (qq1+qq2*t1*sqrt(-log(t2)/t2))**2 
	   if (TestErg < 0 )  goto 100  
	   if (isnan(TestErg)) goto 100 
      endif !rdum(1) DD/DT/TT if test

                                    
      qq2=sqrt(rdum(2)/fudge)/2.0                                       
   !      qq2=sqrt(rdum(2)/1000.0)/2.0                                     
   ! *** define energy of particle                                         
      pbl%r%erg=(qq1+qq2*t1*sqrt(-log(t2)/t2))**2  
      !write(723,*) pbl%r%erg, qq1, qq2, t1,t1                         
   ! *** call D-shape distribution of the particles in the plasma          
!
!cdd      call srgnt(xxx,yyy,zzz,idum,rdum)                                 
      call srgnt                                     
   !    find the number of the cell containing the starting point          
   !    IDUM(*) is the list of possible source cell numbers                
      J = 0                                                             
      DO I=1,IDUM(2)                                                    
         pbl%i%icl = NAMCHG(1,IDUM(I+2))                                      
         CALL CHKCEL(pbl%i%icl,2,J)                                           
         IF (J.EQ.0) GOTO 999                                           
      ENDDO                                                             
 999  CONTINUE                                                          
      if(pbl%i%icl.eq.0.or.j.ne.0)goto 100                                    
  ! 
  return
end subroutine plasma
   ! ---------------------------------------------------------------------
!cdd      subroutine srgnt(xxx,yyy,zzz,idum,rdum)
      subroutine srgnt
  use mcnp_interfaces_mod, only : expirx
  use mcnp_debug
  use mcnp_global
  use mcnp_random
  use mcnp_params, only : DKND
  use pblcom, only : pbl
  use tskcom
  use mcnp_particles, only: neutron
      implicit real(dknd) (a-h,o-z)
!
!cdd      dimension a(256),s(256),idum(50),rdum(50)
      dimension a(256),s(256)
      data icall/0/
!
!PP      data rm,ap,e0,e1,cp0,esh,epk/630.,182.4,1.806,0.364,&
!           &  0.57,21.89,4.0/
      data kb/8/
      save
!	
      if(icall.le.0) then
   ! *** set geometric variables according to input of source card
         rm=rdum(3)
         ap=rdum(4)
         e0=rdum(5)
         e1=0.0
         cp0=rdum(6)
         esh=rdum(7)
         epk=rdum(8)
         deltaz=rdum(9)
   ! *** define some variables
         n1=2**kb
         fn1=n1
         do 10 n=1,n1
            fn=n
            s(n)=(2.*fn1-2.*fn+1.)/(2.*fn1-1.)
            a(n)=ap*sqrt(1.-((fn1-fn+1.)/fn1)**(1./epk))
 10      continue
         icall=icall+1
      endif
   ! *** define r value of particle
 200  r=sqrt((rm-ap)*(rm-ap)+4.*rm*ap*rang())

   ! *** define e
      e=e0+e1

   ! *** use this line for a source above and below midplane
      pbl%r%z=-e*ap+2.*e*ap*rang()

      z=abs(pbl%r%z)
      pbl%r%z=pbl%r%z+deltaz
      x=r-rm
      sint=z/(ap*e)
      t=asin(sint)
      qxd=ap*cos(t+cp0*sint)
      if(x.ge.qxd) goto 200
      qxs=ap*cos(3.141592654-t+cp0*sint)
      if(x.le.qxs) goto 200
      i=2**(kb-1)
      ip=0
      do 20 n=1,kb
         i=i+ip*2**(kb-n)
         ip=+1
         estar=e
         if(z.ge.a(i)*estar) goto 20
         sint=z/(a(i)*estar)
         t=asin(sint)
         cp=cp0
         qxd=a(i)*cos(t+cp*sint)+esh*(1.-(a(i)/ap)**2)
         if(x.ge.qxd) goto 20
         qxs=a(i)*cos(3.141592654-t+cp*sint)+esh*(1.-(a(i)/ap)**2)
         if(x.le.qxs) goto 20
         ip=-1
 20   continue
      ip=max0(0,ip)
      if(rang().gt.s(i+ip)) go to 200
   !
   ! *** define the angle about z axis at which the particle is:
   ! *** 90 degrees about y axis (i.e y is always positive and x is either +ve
   ! *** of -ve)
      FI = (rdum(10)+rdum(11)* RANG())*0.017453292
      pbl%r%x = R * COS(FI)
      pbl%r%y = R * SIN(FI)

  return
end subroutine srgnt
