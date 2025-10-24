using System;

public class Program
{
    public static void Main()
    {
        int[] secret = new int[4];
        Random rand = new Random();

        // Generate secret code (digits 1-9)
        for (int i = 0; i < 4; i++)
        {
            secret[i] = rand.Next(1, 10);
        }

        for (int attempt = 0; attempt < 8; attempt++)
        {
            Console.WriteLine($"\nAttempt {attempt + 1}/8: Enter a 4-digit guess (digits 1–9):");
            string input = Console.ReadLine();

            if (input.Length != 4 || !int.TryParse(input, out _))
            {
                Console.WriteLine("Invalid input. Try again.");
                attempt--;
                continue;
            }

            int[] guess = new int[4];
            for (int i = 0; i < 4; i++)
            {
                guess[i] = (int)Char.GetNumericValue(input[i]);
            }

            char[] feedback = new char[4];
            bool[] secretUsed = new bool[4];
            bool[] guessUsed = new bool[4];

            // First pass: check for exact matches
            for (int i = 0; i < 4; i++)
            {
                if (guess[i] == secret[i])
                {
                    feedback[i] = 'A';
                    secretUsed[i] = true;
                    guessUsed[i] = true;
                }
            }

            // Second pass: check for partial matches
            for (int i = 0; i < 4; i++)
            {
                if (guessUsed[i]) continue;

                bool found = false;
                for (int j = 0; j < 4; j++)
                {
                    if (!secretUsed[j] && guess[i] == secret[j])
                    {
                        found = true;
                        secretUsed[j] = true;
                        break;
                    }
                }

                feedback[i] = found ? 'B' : '_';
            }

            Console.WriteLine("Feedback: " + new string(feedback));

            if (new string(feedback) == "AAAA")
            {
                Console.WriteLine("Congratulations! You guessed the code.");
                return;
            }
        }

        Console.WriteLine("\nGame over! The correct code was: " + string.Join("", secret));
    }
}
