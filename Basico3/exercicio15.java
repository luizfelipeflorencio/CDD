package Basico3;

public class exercicio15 {

	public static void main(String[] args) {
		String texto1[] = {"a", "Vida", "é", "Bela"};
		String texto2 = "";
		for(String a: texto1) {
			texto2+= a+ " "; 
	}
	System.out.println(texto2.toUpperCase());	
}
}