%----------------------------------
% AUTHOR: Nikhil Garg
%----------------------------------

function x_car = CommonAR(input)
	%% Common Average Reference of input signal

	for k = 1:16
		u = mean(input(:,:,k));
		x_car(:,:,k) = input(:,:,k) - u;
	end
end