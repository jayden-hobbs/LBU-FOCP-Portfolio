use std::io;
use std::process;
use rand::Rng;

fn get_player_choice() -> String {
    loop {
        println!("Please enter your choice (rock, paper, or scissors): ");
        let mut player_choice = String::new();
        io::stdin().read_line(&mut player_choice).expect("Failed to read line");
        let player_choice = player_choice.trim();
        if player_choice == "rock" || player_choice == "paper" || player_choice == "scissors" {
            return player_choice.to_string();
        } else {
            println!("Invalid choice. Please enter rock, paper, or scissors.");
        }
    }
}

fn get_computer_choice() -> String {
    let mut rng = rand::thread_rng();
    let computer_number = rng.gen_range(1..=3);
    match computer_number {
        1 => String::from("rock"),
        2 => String::from("paper"),
        _ => String::from("scissors"),
    }
}

fn play_game() {
    let player_choice = get_player_choice();
    let computer_choice = get_computer_choice();

    println!("Player chose: {}", player_choice);
    println!("Computer chose: {}", computer_choice);

    if player_choice == computer_choice {
        println!("It's a tie!");
    } else if (player_choice == "rock" && computer_choice == "scissors") ||
              (player_choice == "paper" && computer_choice == "rock") ||
              (player_choice == "scissors" && computer_choice == "paper") {
        println!("Player wins!");
    } else {
        println!("Computer wins!");
    }
}

fn main() {
    loop {
        play_game();

        println!("Do you want to play again? (y/n)");
        let mut play_again = String::new();
        io::stdin().read_line(&mut play_again).expect("Failed to read line");
        let play_again = play_again.trim().to_lowercase();

        if play_again == "n" {
            println!("Thanks for playing!");
            process::exit(0);
        } else if play_again != "y" {
            println!("Invalid choice. Please enter 'y' or 'n'.");
        }
    }
}