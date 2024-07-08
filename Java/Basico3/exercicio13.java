package Basico3;

public class exercicio13 {

	public static void main(String[] args) {
		String texto1 = "Será que são iguais?";
		String texto2 = "Será que são iguais?";
		
		boolean b1 = texto1.equals(texto2);
		
		if(b1 == true) {
			System.out.println("São iguais");	
		
		}
		else {
			System.out.println("Não são iguais");
		}
		
}
}