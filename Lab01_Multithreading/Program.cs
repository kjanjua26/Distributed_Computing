using System;
using System.Diagnostics;

// Using single thread!
namespace lab01{
    class Program{
        static void Main(string[] args){
            Console.WriteLine("Hello World!");
            var watch = System.Diagnostics.Stopwatch.StartNew();
            calculatePI();
            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine("PI calculation took: {0} miliseconds", elapsedMs);
        }
        static void calculatePI(){
            double x, pi, sum = 0.0;
            double steps;
            long num_step = 100000;
            steps = 1/((double)num_step);
            for(int i = 0; i < num_step; i++){
                x = (i + 0.5) * steps;
                sum = sum + 4.0 / (1 + x*x);
            }
            pi = steps * sum;
            Console.WriteLine("The Value of PI is: {0}", pi);
        }
    }
}
