package Basico3;

import java.util.Scanner;

public class exercicio14 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um texto: ");
		String texto = entrada.nextLine();
		String str = texto;
		String resultado = str.toUpperCase();
		System.out.println(resultado);
	}
}