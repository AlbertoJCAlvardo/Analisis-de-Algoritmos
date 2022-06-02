#include<stdio.h>

float celciusFarenheit(float t);
float farenheitCelcius(float t);
float celciusFarenheit(float t);


int main(void){
	float t,r;
	int op;
	
	printf("1)Convertir grados celcius a farenheit\n2)Convertir grados farenheit a celcius\n\nSu opcion:  ");
	scanf("%d", &op);
	
	switch(op){
		case 1:
			printf("Temperatura en celius: ");
			scanf("%f", &t);
			r = celciusFarenheit(t);
			printf("Resultado:  %.2f farenheit",r);
		break;
		case 2:
			printf("Temperatura en farenheit: ");
			scanf("%f", &t);
			r = farenheitCelcius(t);
			printf("Resultado:  %.2f celcius",r);
		break;
		default:
			printf("Error");
		break;
	}
	
		
}


float celciusFarenheit(float t){
	return t*9/5 + 32;
}
float farenheitCelcius(float t){
	return (t-32)*5/9;
}


