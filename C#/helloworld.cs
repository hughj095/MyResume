using System;

class Program
{
    static void Main(string[] args)
    {
        // Prompt the user to enter their name
        Console.WriteLine("Please enter your name:");

        // Read the user's input from the console
        string name = Console.ReadLine();

        // Greet the user
        Console.WriteLine("Hello, " + name + "! Welcome to the basic C# program.");

        // Keep the console window open until a key is pressed
        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }
}