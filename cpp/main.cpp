#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <sstream>
#include <tuple>

enum AkseedModelOffset {
	kAkseedModelMarvell		= 0,
	kAkseedModelSMN900S		= 51,
	kAkseedModelKorea		= 51,
	kAkseedModelSMN900L		= 71,
	kAkseedModelSMG900L		= 47,
	kAkseedModelSMG900K		= 54,
	kAkseedModelSMG900S		= 73,
	kAkseedModelSHVE470S	= 73,
	kAkseedModelSMN900K		= 61,
	kAkseedModelSHVE250K	= 88,
	kAkseedModelDefault		= 89,
};


std::tuple<int, int, int> akseed_calculate(int number1, int number2, int number3, int addOffset = kAkseedModelDefault);
void usage();
int main(int argc, char** argv);

std::tuple<int, int, int> akseed_calculate(int number1, int number2, int number3, int addOffset)
{
	int i = 1;
	int calc1, calc2, calc3;

	calc1 = number2;
	while (i <= (number3 / 2)){
		calc1 = (((number2 * number2) % number1) * calc1) % number1;
		i++;
	}

	calc1 += addOffset;

	calc2 = round(fmod((number1 * 0x181E5), log(number1))) + addOffset;
	calc3 = round(((number2 * number1) / number1) / log(number2)) + addOffset;

	return std::make_tuple(calc1, calc2, calc3);
}

void usage() {
	printf("AKSEEDNO Challenge Response Calculator\n");
	printf("Created by Gassan Idriss\n");
	printf("License: GPL\n");
	printf("Source: https://github.com/ghassani/akseed-calculator\n");
	printf("\nUsage:\n");
	printf("\t*nix: akseed_calc [num1] [num2] [num3]\n");
	printf("\tWindows: akseed_calc.exe [num1] [num2] [num3]\n");
}

int main(int argc, char** argv) {

	if (argc < 4) {
		usage();
		return 0;
	}

	int a = strtoul(argv[1], NULL, 10);
	int b = strtoul(argv[2], NULL, 10);
	int c = strtoul(argv[3], NULL, 10);

	if (!a || !b || !c) {
		usage();
		return 0;
	}

	printf("Calculating Response For: %d %d %d\n", a, b, c);

	std::tuple<int,int,int> res = akseed_calculate(a, b, c);

	printf("%d-%d-%d\n", std::get<0>(res), std::get<1>(res), std::get<2>(res));

	return 0;
}