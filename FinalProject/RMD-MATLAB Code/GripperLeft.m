a=2; %inches, L2
b=1.59769; % L3
c=2; % L4
d=1.57801; %L1
l2=a;
l3=b;
l4=c;
l1=d;
geardistance=1.74; %distance between gears left and right
fingerwidth=.5; % width of each gripper's finger from top view
%theta2=0*pi/180:pi/180:360*pi/180;
theta2=16.89*pi/180:pi/180:54.8514*pi/180; %  range of theta2 values (need to use offset angle)
omega2=1;
alpha2=0;
k1=d/a;
k2=d/c;
k3=(a^2-b^2+c^2+d^2)/(2*a*c);
A=cos(theta2)-k1-(k2*cos(theta2))+k3;
B=-2*sin(theta2);
C=k1-((k2+1)*cos(theta2))+k3;
%theta4=2*atan2(-B+sqrt(B.^2-(4*A.*C)),2*A); %for crossed circuit
theta4=2*atan2(-B-sqrt(B.^2-(4*A.*C)),2*A); %for open circuit
k4=l1/l3;
k5=(l4^2-l1^2-l2^2-l3^2)/(2*l2*l3);
D=cos(theta2)-k1+(k4*cos(theta2))+k5;
E=-2*sin(theta2);
F=k1+((k4-1)*cos(theta2))+k5;
%theta3=2*atan2(-E+sqrt(E.^2-(4*D.*F)),2*D); % for crossed circuit
theta3=2*atan2(-E-sqrt(E.^2-(4*D.*F)),2*D); % for open circuit
pointB_X=cos(theta2)+cos(theta3);
pointB_Y=sin(theta2)+sin(theta3);
%global XY frame (73.11 degree shift)
pointB_Xglobal=cos(theta2+(73.11*pi/180))+cos(theta3+(73.11*pi/180));
pointB_Yglobal=sin(theta2+(73.11*pi/180))+sin(theta3+(73.11*pi/180));
gripperopeningwidth=geardistance-(2.*pointB_Xglobal)-fingerwidth;

theta2=theta2*180/pi;
theta3=theta3*180/pi;
theta4=theta4*180/pi;
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
ylabel('pointB_X, global gripper X position (inches)')
figure(6)
plot(theta2,pointB_Yglobal)
xlabel('theta2 (deg)')
ylabel('pointB_Y, global gripper Y position (inches)')
figure(7)
plot(theta2,gripperopeningwidth)
xlabel('theta2 (deg)')
ylabel('gripper opening width (inches)')
theta2=theta2*pi/180;
theta3=theta3*pi/180;
theta4=theta4*pi/180;

% Velocity analysis
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
