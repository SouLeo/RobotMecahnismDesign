a=4.38; %inches, L2
b=7.74662; % L3
c=2.36828; % L4
d=11.6578; %L1
l2=a;
l3=b;
l4=c;
l1=d;
%theta2=0*pi/180:pi/180:360*pi/180;
theta2global=-56.5663*pi/180:pi/180:-1.2355*pi/180; %  range of theta2 values (need to use offset angle)
delta=-51.12802555*pi/180:.76*pi/180:-9.308388803*pi/180; % increments ensure # of delta values matches # of theta2 values. angle offset O2(grounded top green) and O4(moving bevel gear)
i=1:1:56;
theta2(i)=theta2global(i)-delta(i);
omega2=1;
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

%Switch to program "B4BartoGripperLeft1.m" for connection between initial
%B4Bar theta2global angle to Gripper thetas and openings


theta2=theta2*180/pi;
theta2global=theta2global*180/pi;
theta3=theta3*180/pi;
theta4=theta4*180/pi;
theta4global=theta4global*180/pi
Griptheta2=Griptheta2*180/pi;
figure(1)
plot(theta2,theta3)
xlabel('theta2 (deg)')
ylabel('theta3 (deg)')
figure(2)
plot(theta2,theta4)
xlabel('theta2 (deg)')
ylabel('theta4 (deg)')
% figure(3)
% plot(theta2,pointB_X)
% xlabel('theta2 (deg)')
% ylabel('pointB_X, gripper X position (inches)')
% figure(4)
% plot(theta2,pointB_Y)
% xlabel('theta2 (deg)')
% ylabel('pointB_Y, gripper Y position (inches)')
figure(5)
plot(theta2,pointB_Xglobal)
xlabel('theta2 (deg)')
ylabel('pointB_Xglobal (inches)')
figure(6)
plot(theta2,pointB_Yglobal)
xlabel('theta2 (deg)')
ylabel('pointB_Yglobal (inches)')
figure(7)
plot(theta2,theta4global)
xlabel('theta2 (deg)')
ylabel('theta4global (deg)')

figure(8)
plot(theta2global,theta4global)
xlabel('theta2global (deg)')
ylabel('theta4global (deg)')

% figure(7)
% plot(theta2,gripperopeningwidth)
% xlabel('theta2 (deg)')
% ylabel('gripper opening width (inches)')
figure(9)
plot(theta2global,Griptheta2)
xlabel('theta2global (deg)')
ylabel('Griptheta2 (deg)')

theta2=theta2*pi/180;
theta2global=theta2global*pi/180;
theta3=theta3*pi/180;
theta4=theta4*pi/180;
theta4global=theta4global*pi/180;
Griptheta2=Griptheta2*pi/180;

% Velocity analysis,  did for GriperLeft1
omega3=(a.*omega2./b).*(sin(theta4-theta2))./(sin(theta3-theta4));
omega4=(a.*omega2./c).*(sin(theta2-theta3))./(sin(theta4-theta3));

%Velocity plots
% theta2=theta2*180/pi;
% figure(5)
% plot(theta2,omega3)
% xlabel('theta2 (deg)')
% ylabel('omega3 (rad/s)')
% figure(6)
% plot(theta2,omega4)
% xlabel('theta2 (deg)')
% ylabel('omega4 (rad/s)')
% theta2=theta2*pi/180;

% Acceleration analysis
accA=c*sin(theta4);
accB=b*sin(theta3);
accD=c*cos(theta4);
accE=b*cos(theta3);
accC=a.*alpha2.*sin(theta2)+a.*omega2.^2.*cos(theta2)+b.*omega3.^2.*cos(theta3)-c.*omega4.^2.*cos(theta4);
accF=a.*alpha2.*cos(theta2)-a.*omega2.^2.*sin(theta2)-b.*omega3.^2.*sin(theta3)+c.*omega4.^2.*sin(theta4);
alpha3=(accC.*accD-accA.*accF)./(accA.*accE-accB.*accD);
alpha4=(accC.*accE-accB.*accF)./(accA.*accE-accB.*accD);

% Acceleration plots
% theta2=theta2*180/pi;
% figure(7)
% plot(theta2,alpha3)
% xlabel('theta2 (deg)')
% ylabel('alpha3 (rad/s^2)')
% figure(8)
% plot(theta2,alpha4)
% xlabel('theta2 (deg)')
% ylabel('alpha4 (rad/s^2)')
% theta2=theta2*pi/180;
