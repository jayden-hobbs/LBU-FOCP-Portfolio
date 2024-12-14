def get_player_choice
  puts "Choose rock (r), paper (p), or scissors (s):"
  player_choice = gets.chomp.downcase
  until ['r', 'p', 's'].include?(player_choice)
    puts "Invalid choice. Choose rock (r), paper (p), or scissors (s):"
    player_choice = gets.chomp.downcase
  end
  player_choice
end

def get_computer_choice
  computer_choice = ['r', 'p', 's'].sample
  computer_choice
end

def choice_to_string(choice)
  case choice
  when 'r'
    'Rock'
  when 'p'
    'Paper'
  when 's'
    'Scissors'
  end
end

def play_game(player_choice, computer_choice)
  player_choice_str = choice_to_string(player_choice)
  computer_choice_str = choice_to_string(computer_choice)

  puts "You chose #{player_choice_str}."
  puts "The computer chose #{computer_choice_str}."

  if player_choice == computer_choice
    puts "It's a tie!"

  elsif player_choice == 'r' && computer_choice == 's' ||
        player_choice == 'p' && computer_choice == 'r' ||
        player_choice == 's' && computer_choice == 'p'
    puts "You win!"
  else
    puts "You lose!"
  end
end

def main
  loop do
    player_choice = get_player_choice
    computer_choice = get_computer_choice
    play_game(player_choice, computer_choice)
    
    loop do
      puts "Do you want to play again? (y/n)"
      play_again = gets.chomp.downcase
      if play_again == "y"
        break
      elsif play_again == "n"
        puts "Exiting game... Goodbye!"
        exit
      else
        puts "Invalid input. Please enter 'y' or 'n'."
      end
    end
  end
end

main