import java.util.Scanner;
import java.util.Random;

public class RockPaperScissors {
    private String playerChoice;
    private String computerChoice;

    public void getPlayerChoice() {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your choice: rock (r), paper (p), or scissors (s): ");
        char choice = Character.toLowerCase(scanner.next().charAt(0));

        switch (choice) {
            case 'r':
                playerChoice = "Rock";
                break;
            case 'p':
                playerChoice = "Paper";
                break;
            case 's':
                playerChoice = "Scissors";
                break;
            default:
                System.out.println("Invalid choice. Please try again.");
                getPlayerChoice();
                return;
        }
    }

    public void getComputerChoice() {
        Random random = new Random();
        int choice = random.nextInt(3);

        switch (choice) {
            case 0:
                computerChoice = "Rock";
                break;
            case 1:
                computerChoice = "Paper";
                break;
            case 2:
                computerChoice = "Scissors";
                break;
        }
    }
    
    public void playGame() {
        getPlayerChoice();
        getComputerChoice();
        getWinner();
    }

    public void getWinner() {
        System.out.println("Player's choice: " + playerChoice);
        System.out.println("Computer's choice: " + computerChoice);

        if (playerChoice.equals(computerChoice)) {
            System.out.println("It's a tie!");
        } else if (playerChoice.equals("Rock") && computerChoice.equals("Scissors") ||
                playerChoice.equals("Paper") && computerChoice.equals("Rock") ||
                playerChoice.equals("Scissors") && computerChoice.equals("Paper")) {
            System.out.println("Player wins!");
        } else {
            System.out.println("Computer wins!");
        }
    }

    public static void main(String[] args) {
        RockPaperScissors game = new RockPaperScissors();
        Scanner scanner = new Scanner(System.in);

        do {
            game.playGame();
            System.out.println("Do you want to play again? (y/n): ");
        } while (scanner.next().equalsIgnoreCase("y"));

        System.out.println("Thanks for playing!");
        scanner.close();
    }
}
