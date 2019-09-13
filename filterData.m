%----------------------------------
% AUTHOR: Nikhil Garg
%----------------------------------

filter1 = filter_7_12_250_bp;
%filter2 = filter_8_30_250_bp;

x_filter = zeros(C,T,S);


for k = 1:S
	for i = 1:C
		x_filter(i,:,k) = wkeep(conv(filter1.Numerator,x(i,:,k)),1500);
	end
end
