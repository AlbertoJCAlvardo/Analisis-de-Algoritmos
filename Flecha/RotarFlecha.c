#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int** generarFlecha(int size);
int** rotar(int **im, int size);
int menu(void);
void imprimirImagen(int **im, int size);
int** Rotar(int** im,int size);

int main(void){
	menu();
	
}

int menu(void){
	int size, **im, sw;
	printf("\n\tROTADOR DE IMAGENES\n\n");
	printf("Inserta la potencia de 2 para dar tamaño a la imagen:  ");
	scanf("%d", &size);
	if(size>0){
		im = generarFlecha(size);
		
		imprimirImagen(im, size);
	}
	
	do{
		
		im = Rotar(im, size);
		imprimirImagen(im, size);
		
		printf("Rotar?\n\n1)Si\t2)No\n\n");
		scanf("%d", &sw);
	}
	while(sw == 1);
	
}




int** generarFlecha(int size){
	int i,j;
	int tam;
	int **im=NULL;
	
	tam = pow(2, size);
	
	im = (int**) malloc (tam * sizeof(int*));
	
	for(i = 0; i<tam; i++)
		im[i] = (int*) malloc (tam * sizeof (int));
		
	for(i = 0; i<tam; i++)
		for(j = 0; j<tam; j++){
			if((i == 0 && j<tam-1)|| (j == 0 && i<tam-1)) 
				im[i][j] = 1;
			else{
				if(i == j || i == j-1 || i == j -1)
					im[i][j] = 1;
				else
					im [i][j] = 0;	
			}
			
		}
		
	return im;
}


void imprimirImagen(int** im,int size){
	int i = 0, j = 0;
	
	int tam;
	tam  = pow(2, size);
	
	for(i = 0; i<tam; i++){
		printf("\t");
		for(j =0; j<tam; j++){
			if(im[i][j] == 0)
				printf("%c", 32);
			if(im[i][j] == 1)
				printf("%c", 219);
				
			
		}
		printf("\n");
	}
}

int **Rotar(int** im,int size){
	int **rot, tam, i, j, k=0, l=0;
	
	tam  = pow(2, size);
	
	rot = generarFlecha(size);
	
	for(i = 0; i<tam; i++){
		
		for(j = 0; j<tam; j++){
			rot[j][tam-1-i] = im[i][j];
			
			
		}
		
		
	}
	
	return rot;
	
}



