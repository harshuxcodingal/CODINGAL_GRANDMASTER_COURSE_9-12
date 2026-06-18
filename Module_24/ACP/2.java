public class Main {

    public static void main(String[] args) {

        String[] wonders = {
            "Great Wall of China",
            "Petra",
            "Christ the Redeemer",
            "Machu Picchu",
            "Chichen Itza",
            "Colosseum",
            "Taj Mahal"
        };

        System.out.println("===== 7 WONDERS OF THE WORLD =====");

        for(int i = 0; i < wonders.length; i++) {
            System.out.println((i + 1) + ". " + wonders[i]);
        }
    }
}