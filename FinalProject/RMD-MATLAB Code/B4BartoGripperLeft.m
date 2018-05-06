a=4.38; %inches, L2
b=7.74662; % L3
c=2.36828; % L4
d=11.6578; %L1
l2=a;
l3=b;
l4=c;
l1=d;
%theta2=0*pi/180:pi/180:360*pi/180;
theta2global=-56.5663*pi/180:pi/180:-1.2355*pi/180; % range of theta2 values (need to use offset angle)
delta=-51.12802555*pi/180:.76*pi/180:-9.308388803*pi/180; % increments ensure # of delta values matches # of theta2 values. angle offset O2(grounded top green) and O4(moving bevel gear)
i=1:1:56;
theta2(i)=theta2global(i)-delta(i);
omega2=1;
Gripomega2=1;
alpha2=0;
k1=d/a;
k2=d/c;
k3=(a^2-b^2+c^2+d^2)/(2*a*c);
A=cos(theta2)-k1-(k2*cos(theta2))+k3;
B=-2*sin(theta2);
C=k1-((k2+1)*cos(theta2))+k3;
theta4=2*atan2(-B+sqrt(B.^2-(4*A.*C)),2*A); %for crossed circuit
%theta4=2*atan2(-B-sqrt(B.^2-(4*A.*C)),2*A); %for open circuit
k4=l1/l3;
k5=(l4^2-l1^2-l2^2-l3^2)/(2*l2*l3);
D=cos(theta2)-k1+(k4*cos(theta2))+k5;
E=-2*sin(theta2);
F=k1+((k4-1)*cos(theta2))+k5;
theta3=2*atan2(-E+sqrt(E.^2-(4*D.*F)),2*D); % for crossed circuit
%theta3=2*atan2(-E-sqrt(E.^2-(4*D.*F)),2*D); % for open circuit
pointB_X=cos(theta2)+cos(theta3);
pointB_Y=sin(theta2)+sin(theta3);

pointO4_Xglobal=d*cos(-delta);
pointO4_Yglobal=d*sin(-delta);
%global XY frame (shift by delta(i))
pointB_Xglobal=cos(theta2+(delta))+cos(theta3+(delta));
pointB_Yglobal=sin(theta2+(delta))+sin(theta3+(delta));

%bevel angle(global) calculation
theta4global=atan2(pointB_Yglobal-pointO4_Yglobal,pointB_Xglobal-pointO4_Xglobal);



%Input gripper left gear angular position given bevel angular position
Griptheta2=theta4global+(150.3709*(pi/180));
%put in all gripper motion stuff into this file so it has the input theta2
%motion of green bar giving the gripper opening width and global X and
%global Y position of the gripper relative to the initial green bar coord
%system (this gives global height and X location of gripper for pickup of
%item, plot gripper stuff vs initial green bar theta2global

%START of GripperLeft1 stuff

Gripa=2; %inches, L2
Gripb=1.59769; % L3
Gripc=2; % L4
Gripd=1.57801; %L1
Gripl2=Gripa;
Gripl3=Gripb;
Gripl4=Gripc;
Gripl1=Gripd;
geardistance=1.74; %distance between gears left and right
fingerwidth=.5; % width of each gripper's finger from top view
%theta2=0*pi/180:pi/180:360*pi/180;
%theta2=16.89*pi/180:pi/180:54.8514*pi/180; %  range of theta2 values (need to use offset angle)
Gripomega2=1;
Gripalpha2=0;
Gripk1=Gripd/Gripa;
Gripk2=Gripd/Gripc;
Gripk3=(Gripa^2-Gripb^2+Gripc^2+Gripd^2)/(2*Gripa*Gripc);
GripA=cos(Griptheta2)-Gripk1-(Gripk2*cos(Griptheta2))+Gripk3;
GripB=-2*sin(Griptheta2);
GripC=Gripk1-((Gripk2+1)*cos(Griptheta2))+Gripk3;
%theta4=2*atan2(-B+sqrt(B.^2-(4*A.*C)),2*A); %for crossed circuit
Griptheta4=2*atan2(-GripB-sqrt(GripB.^2-(4*GripA.*GripC)),2*GripA); %for open circuit
Gripk4=Gripl1/Gripl3;
Gripk5=(Gripl4^2-Gripl1^2-Gripl2^2-Gripl3^2)/(2*Gripl2*Gripl3);
GripD=cos(Griptheta2)-Gripk1+(Gripk4*cos(Griptheta2))+Gripk5;
GripE=-2*sin(Griptheta2);
GripF=Gripk1+((Gripk4-1)*cos(Griptheta2))+Gripk5;
%theta3=2*atan2(-E+sqrt(E.^2-(4*D.*F)),2*D); % for crossed circuit
Griptheta3=2*atan2(-GripE-sqrt(GripE.^2-(4*GripD.*GripF)),2*GripD); % for open circuit
GrippointB_X=cos(Griptheta2)+cos(Griptheta3);
GrippointB_Y=sin(Griptheta2)+sin(Griptheta3);
%global XY frame (73.11 degree shift)
GrippointB_Xglobal=cos(Griptheta2+(73.11*pi/180))+cos(Griptheta3+(73.11*pi/180));
GrippointB_Yglobal=sin(Griptheta2+(73.11*pi/180))+sin(Griptheta3+(73.11*pi/180));
gripperopeningwidth=geardistance-(2.*GrippointB_Xglobal)-fingerwidth;

Griptheta2=Griptheta2*180/pi;
Griptheta3=Griptheta3*180/pi;
Griptheta4=Griptheta4*180/pi;
theta2global=theta2global*180/pi;
figure(1)
plot(Griptheta2,Griptheta3)
xlabel('Griptheta2 (deg)')
ylabel('Griptheta3 (deg)')
figure(2)
plot(Griptheta2,Griptheta4)
xlabel('Griptheta2 (deg)')
ylabel('Griptheta4 (deg)')
% figure(3)
% plot(theta2,pointB_X)
% xlabel('theta2 (deg)')
% ylabel('pointB_X, gripper X position (inches)')
% figure(4)
% plot(theta2,pointB_Y)
% xlabel('theta2 (deg)')
% ylabel('pointB_Y, gripper Y position (inches)')
figure(5)
plot(Griptheta2,GrippointB_Xglobal)
xlabel('Griptheta2 (deg)')
ylabel('pointB_X, global gripper X position (inches)')
figure(6)
plot(Griptheta2,GrippointB_Yglobal)
xlabel('Griptheta2 (deg)')
ylabel('pointB_Y, global gripper Y position (inches)')
figure(7)
plot(Griptheta2,gripperopeningwidth)
xlabel('Griptheta2 (deg)')
ylabel('gripper opening width (inches)')
%STARTing plots of Grip stuff vs. theta2global of B4Bar
figure(8)
plot(theta2global,Griptheta2)
xlabel('theta2global (deg)')
ylabel('Griptheta2 (deg)')
figure(9)
plot(theta2global,Griptheta3)
xlabel('theta2global (deg)')
ylabel('Griptheta3 (deg)')
figure(10)
plot(theta2global,Griptheta4)
xlabel('theta2global (deg)')
ylabel('Griptheta4 (deg)')
figure(11)
plot(theta2global,GrippointB_Xglobal)
xlabel('theta2global (deg)')
ylabel('pointB_X, global gripper X position (inches)')
figure(12)
plot(theta2global,GrippointB_Yglobal)
xlabel('theta2global (deg)')
ylabel('pointB_Y, global gripper Y position (inches)')
figure(13)
plot(theta2global,gripperopeningwidth)
xlabel('theta2global (deg)')
ylabel('gripper opening width (inches)')
%ENDing plots of Grip stuff vs. theta2global of B4Bar

Griptheta2=Griptheta2*pi/180;
Griptheta3=Griptheta3*pi/180;
Griptheta4=Griptheta4*pi/180;
theta2global=theta2global*pi/180;

% Velocity analysis
omega3=(a.*omega2./b).*(sin(Griptheta4-Griptheta2))./(sin(Griptheta3-Griptheta4));
omega4=(a.*omega2./c).*(sin(Griptheta2-Griptheta3))./(sin(Griptheta4-Griptheta3));
Gripomega3=(Gripa.*Gripomega2./Gripb).*(sin(Griptheta4-Griptheta2))./(sin(Griptheta3-Griptheta4));
Gripomega4=(Gripa.*Gripomega2./Gripc).*(sin(Griptheta2-Griptheta3))./(sin(Griptheta4-Griptheta3));

%Velocity plots
 theta2=theta2*180/pi;
 Griptheta2=theta2*180/pi;
 
 figure(14)
 plot(theta2,omega3)
 xlabel('theta2 (deg)')
 ylabel('omega3 (rad/s)')
 figure(15)
 plot(theta2,omega4)
 xlabel('theta2 (deg)')
 ylabel('omega4 (rad/s)')
 
 figure(16)
 plot(Griptheta2,Gripomega3)
 xlabel('Griptheta2 (deg)')
 ylabel('Gripomega3 (rad/s)')
 figure(17)
 plot(Griptheta2,Gripomega4)
 xlabel('Griptheta2 (deg)')
 ylabel('Gripomega4 (rad/s)')
 
 Griptheta2=Griptheta2*pi/180;
 theta2=theta2*pi/180;

% Acceleration analysis
accA=c*sin(theta4);
accB=b*sin(theta3);
accD=c*cos(theta4);
accE=b*cos(theta3);
accC=a.*alpha2.*sin(theta2)+a.*omega2.^2.*cos(theta2)+b.*omega3.^2.*cos(theta3)-c.*omega4.^2.*cos(theta4);
accF=a.*alpha2.*cos(theta2)-a.*omega2.^2.*sin(theta2)-b.*omega3.^2.*sin(theta3)+c.*omega4.^2.*sin(theta4);
alpha3=(accC.*accD-accA.*accF)./(accA.*accE-accB.*accD);
alpha4=(accC.*accE-accB.*accF)./(accA.*accE-accB.*accD);

GripaccA=Gripc*sin(Griptheta4);
GripaccB=Gripb*sin(Griptheta3);
GripaccD=Gripc*cos(Griptheta4);
GripaccE=Gripb*cos(Griptheta3);
GripaccC=Gripa.*Gripalpha2.*sin(Griptheta2)+Gripa.*Gripomega2.^2.*cos(Griptheta2)+Gripb.*Gripomega3.^2.*cos(Griptheta3)-Gripc.*Gripomega4.^2.*cos(Griptheta4);
GripaccF=Gripa.*Gripalpha2.*cos(Griptheta2)-Gripa.*Gripomega2.^2.*sin(Griptheta2)-Gripb.*Gripomega3.^2.*sin(Griptheta3)+Gripc.*Gripomega4.^2.*sin(Griptheta4);
Gripalpha3=(GripaccC.*GripaccD-GripaccA.*GripaccF)./(GripaccA.*GripaccE-GripaccB.*GripaccD);
Gripalpha4=(GripaccC.*GripaccE-GripaccB.*GripaccF)./(GripaccA.*GripaccE-GripaccB.*GripaccD);

% Acceleration plots
 theta2=theta2*180/pi;
 Griptheta2=Griptheta2*180/pi;
 
 figure(18)
 plot(theta2,alpha3)
 xlabel('theta2 (deg)')
 ylabel('alpha3 (rad/s^2)')
 figure(19)
 plot(theta2,alpha4)
 xlabel('theta2 (deg)')
 ylabel('alpha4 (rad/s^2)')
 
 figure(20)
 plot(Griptheta2,Gripalpha3)
 xlabel('Griptheta2 (deg)')
 ylabel('Gripalpha3 (rad/s^2)')
 figure(21)
 plot(Griptheta2,Gripalpha4)
 xlabel('Griptheta2 (deg)')
 ylabel('Gripalpha4 (rad/s^2)')
 
 Griptheta2=Griptheta2*pi/180;
 theta2=theta2*pi/180;

 %STARTing B4Bar theta2global plots for velocity and acceleration of B4Bar stuff
 theta2global=theta2global*180/pi;
 figure(22)
 plot(theta2global,omega3)
 xlabel('theta2global (deg)')
 ylabel('omega3 (rad/s)')
 figure(23)
 plot(theta2global,omega4)
 xlabel('theta2global (deg)')
 ylabel('omega4 (rad/s)')
 
 figure(24)
 plot(theta2global,alpha3)
 xlabel('theta2global (deg)')
 ylabel('alpha3 (rad/s^2)')
 figure(25)
 plot(theta2global,alpha4)
 xlabel('theta2global (deg)')
 ylabel('alpha4 (rad/s^2)')
 theta2global=theta2global*pi/180;
 
 %ENDing B4Bar theta2global plots for velocity and acceleration of B4Bar stuff

 %Go to "B4BarVelAcctoVelAccGripperLeft1.m" for relating stuff from
 %original B4Bar velocity and acc to Gripper vel and acc stuff
 
%END of GripperLeft1 stuff

% Griptheta2=Griptheta2*180/pi;
% Griptheta2global=Griptheta2global*180/pi;
% Griptheta3=Griptheta3*180/pi;
% Griptheta4=Griptheta4*180/pi;
% Griptheta4global=Griptheta4global*180/pi
% Griptheta2=Griptheta2*180/pi;
% figure(1)
% plot(Griptheta2,Griptheta3)
% xlabel('Griptheta2 (deg)')
% ylabel('Griptheta3 (deg)')
% figure(2)
% plot(Griptheta2,Griptheta4)
% xlabel('Griptheta2 (deg)')
% ylabel('Griptheta4 (deg)')
% % figure(3)
% % plot(theta2,pointB_X)
% % xlabel('theta2 (deg)')
% % ylabel('pointB_X, gripper X position (inches)')
% % figure(4)
% % plot(theta2,pointB_Y)
% % xlabel('theta2 (deg)')
% % ylabel('pointB_Y, gripper Y position (inches)')
% figure(5)
% plot(Griptheta2,pointB_Xglobal)
% xlabel('Griptheta2 (deg)')
% ylabel('pointB_Xglobal (inches)')
% figure(6)
% plot(Griptheta2,pointB_Yglobal)
% xlabel('Griptheta2 (deg)')
% ylabel('pointB_Yglobal (inches)')
% figure(7)
% plot(Griptheta2,Griptheta4global)
% xlabel('Griptheta2 (deg)')
% ylabel('Griptheta4global (deg)')
% 
% figure(8)
% plot(Griptheta2global,Griptheta4global)
% xlabel('Griptheta2global (deg)')
% ylabel('Griptheta4global (deg)')
% 
% % figure(7)
% % plot(theta2,gripperopeningwidth)
% % xlabel('theta2 (deg)')
% % ylabel('gripper opening width (inches)')
% figure(9)
% plot(Griptheta2global,Griptheta2)
% xlabel('Griptheta2global (deg)')
% ylabel('Griptheta2 (deg)')
% 
% Griptheta2=Griptheta2*pi/180;
% Griptheta2global=Griptheta2global*pi/180;
% Griptheta3=Griptheta3*pi/180;
% Griptheta4=Griptheta4*pi/180;
% Griptheta4global=Griptheta4global*pi/180;
% Griptheta2=Griptheta2*pi/180;
% 
% % Velocity analysis,  did for GriperLeft1
% % omega3=(a.*omega2./b).*(sin(theta4-theta2))./(sin(theta3-theta4));
% % omega4=(a.*omega2./c).*(sin(theta2-theta3))./(sin(theta4-theta3));
% 
% %Velocity plots
% % theta2=theta2*180/pi;
% % figure(5)
% % plot(theta2,omega3)
% % xlabel('theta2 (deg)')
% % ylabel('omega3 (rad/s)')
% % figure(6)
% % plot(theta2,omega4)
% % xlabel('theta2 (deg)')
% % ylabel('omega4 (rad/s)')
% % theta2=theta2*pi/180;
% 
% % Acceleration analysis
% % accA=c*sin(theta4);
% % accB=b*sin(theta3);
% % accD=c*cos(theta4);
% % accE=b*cos(theta3);
% % accC=a.*alpha2.*sin(theta2)+a.*omega2.^2.*cos(theta2)+b.*omega3.^2.*cos(theta3)-c.*omega4.^2.*cos(theta4);
% % accF=a.*alpha2.*cos(theta2)-a.*omega2.^2.*sin(theta2)-b.*omega3.^2.*sin(theta3)+c.*omega4.^2.*sin(theta4);
% % alpha3=(accC.*accD-accA.*accF)./(accA.*accE-accB.*accD);
% % alpha4=(accC.*accE-accB.*accF)./(accA.*accE-accB.*accD);
% 
% % Acceleration plots
% % theta2=theta2*180/pi;
% % figure(7)
% % plot(theta2,alpha3)
% % xlabel('theta2 (deg)')
% % ylabel('alpha3 (rad/s^2)')
% % figure(8)
% % plot(theta2,alpha4)
% % xlabel('theta2 (deg)')
% % ylabel('alpha4 (rad/s^2)')
% % theta2=theta2*pi/180;
