using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string x = Console.ReadLine();
            string y = Console.ReadLine();
            string z = Console.ReadLine();
            DateTime date1 = DateTime.Parse(x, System.Globalization.CultureInfo.CurrentCulture);
            DateTime date2 = DateTime.Parse(y, System.Globalization.CultureInfo.CurrentCulture);
            DateTime date3 = DateTime.Parse(z, System.Globalization.CultureInfo.CurrentCulture);

            TimeSpan diff = date3 - date1;
            if (diff < TimeSpan.Zero)
            {
                diff += TimeSpan.FromDays(1);
            }

            var value = TimeSpan.FromSeconds(Math.Floor((diff.TotalSeconds + 1) / 2));
            var exit = date2 + value;
            Console.WriteLine(exit.ToString("HH:mm:ss"));
            Console.ReadKey();
        }
    }
}