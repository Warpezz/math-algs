namespace app;

public class PrimesFinder
{
    public static List<int> primesFinder(int amountWanted)
    {
        List<int> primesList = new List<int>();
        int numToTest = 2;
        while (primesList.Count() < amountWanted)
        {
            bool isPrime = true;
            int divisor =  numToTest - 1;
            while (divisor > 1)
            {
                if ((numToTest % divisor) == 0)
                {
                    isPrime = false;
                }
                divisor--;
            }
            if (isPrime == true)
            {
                primesList.Add(numToTest);
            }
            numToTest++;
        }

        return primesList;
    }

    static bool IsAllDigits(string? _string)
    {
        if (_string == null || _string == "")
        {
            return false;
        }
        bool areAllDigits = true;
        foreach(char _ in _string)
        {
            if (!Char.IsDigit(_))
            {
                areAllDigits = false;
                break;
            }
        }
        return areAllDigits;
    }

    static void PrintIterateList<T>(List<T> _list)
    {
        string output = "[";
        foreach (var _ in _list)
        {
            output += ("\'" + (_!.ToString() ?? "null") + "\', ");
        }
        output += "]";
        Console.WriteLine(output);
    }

    public static void PrimesPrompt()
    {
        Console.WriteLine("How many primes do you want to output? (default 5)");
        string? input = Console.ReadLine();
        int amountWanted;
        if (IsAllDigits(input) == true)
        {
            amountWanted = Int32.Parse(input ?? "5");
        } else 
        {
            Console.WriteLine("input is invalid or non-numeric");
            amountWanted = 5;
        }
        List<int> primesList = primesFinder(amountWanted);
        Console.WriteLine("Primes:");
        PrintIterateList<int>(primesList);
    }
}