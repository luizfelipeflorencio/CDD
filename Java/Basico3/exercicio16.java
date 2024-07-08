package Basico3;

public class exercicio16 {

	public static void main(String[] args) {
		String caracteres[] = {"a", "Vida", "é", "Bela"};
		
		for(int i = caracteres.length-1; i>=0; i--) {
			String texto = caracteres[i].toUpperCase();
			System.out.print(texto + " ");
		}

	}

}
