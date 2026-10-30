import java.util.Scanner;


public class App {

    public static final Scanner SC = new Scanner(System.in); 

    public static void main(String[] args) throws Exception {
        
        Unidade unidadeOriginal = selecionarUnidade("ser a unidade original");

        System.out.println("Insira um valor em " + unidadeOriginal.getDescricao());
        float distancia = SC.nextFloat();

        Unidade unidadeDestino = selecionarUnidade("ser a unidade destino");

        float distanciaEmMetro = transformarEmMetro(distancia, unidadeOriginal);

        float resultado;

        switch (unidadeDestino) {
            case METRO:
                resultado = distancia;
                break;
        
            case QUILOMETRO :
                resultado = distancia / 1000;
                break;

            case PE :
                resultado = distancia * 3.28084f;
                break;

            case MILHA :
                resultado = distancia / 1609.344f;

            default:
                throw new IllegalArgumentException("Unidade não reconhecida");
        }

        System.out.println(distancia + " " + unidadeOriginal + " em " + unidadeDestino + " é " + resultado + " " + unidadeDestino);
        
    }

    public static Unidade selecionarUnidade(String objetivo) {

        Unidade unidade;

        
        for (int i = 0; i < Unidade.values().length; i++) {
            System.out.println((i + 1) + " - " + Unidade.values()[i].getDescricao());
        }

        System.out.print("Selecione uma unidade de medida para " + objetivo + ": ");
        unidade = Unidade.values()[SC.nextInt() - 1];

        return unidade;
    }

    public static float transformarEmMetro(float distancia, Unidade unidadeOriginal) {
        switch (unidadeOriginal) {
            case METRO : return distancia;
            case QUILOMETRO : return distancia * 1000;
            case PE : return distancia * 0.3048f;
            case MILHA : return distancia * 1609.344f;
            default : throw new IllegalArgumentException("Unidade não reconhecida");
        }
    }
}
