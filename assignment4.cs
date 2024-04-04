using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int[] numbers = { 1, 2, 2, 3, 3, 3, 4, 4, 4, 4 };
        Dictionary<int, int> frequencyMap = new Dictionary<int, int>();

        // Count the frequency of each unique element
        foreach (int num in numbers)
        {
            if (frequencyMap.ContainsKey(num))
            {
                frequencyMap[num]++;
            }
            else
            {
                frequencyMap[num] = 1;
            }
        }

        // Print the elements and their frequencies
        foreach (var pair in frequencyMap)
        {
            Console.WriteLine($"Element: {pair.Key}, Frequency: {pair.Value}");
        }
    }
}