clear all
clc
close all
name='';
A = importdata(name);

dir=cd;
[l a]=size(A)

figure(1)
plot(A(:,1))
title('Cooling Schedule')
xlabel('time')
ylabel('Temperature')
save1=strcat(dir,'/',name,'coolin_sched','.png');
saveas(figure(1),save1);




figure(2)
for i=2:a
    plot(A(:,i),'*-')
    hold on
end
xlabel('Time')
ylabel('Energy')
save2=strcat(dir,'/',name,'all_ener','.png');
saveas(figure(2),save2)



figure(3)
plot(A(1:l-2,2))%A19 for one of several ground states
xlabel('Time')
ylabel('Energy')
save3=strcat(dir,'/',name,'_1_sample','.png');
saveas(figure(3),save3)


%calculate averages at temperatures
for j=2:l
    M(j)=mean(A(j,:));
end

figure(4)
plot(M)
ylabel('Energy')
xlabel('Time (Monte Carlo Steps)')
save4=strcat(dir,'/',name,'_aver_ener','.png');
saveas(figure(4),save4);


figure(5)
histogram(A(:,2:a))
xlabel('Energies')
save5=strcat(dir,'/',name,'_energ_dist','.png');
saveas(figure(5),save5);

figure(6)
plot(A(:,1),M,'.-')
ylabel('Energy')
xlabel('Temperature')
save6=strcat(dir,'/',name,'ener_vs_temp','.png');
saveas(figure(6),save6);
%%
Nsaw=5.7683e+09;
f=histogram(A(:,2:a));
p=f.Values;
E=0:-1:-length(p)+1;
%p=fliplr(p);
%E=fliplr(E);
T=.5;


for kk=1:length(p)
    g(kk)=1/350*(p(kk)*exp(-E(kk)/T));
end

% figure(7)
% bar(E,fliplr(g))
% xlabel('Energy')
% ylabel('Number of States')
figure(8)
semilogy(E,fliplr(g),'*')
save8=strcat(dir,'/',name,'ener_distribution','.png');
saveas(figure(8),save8);
g(1)
