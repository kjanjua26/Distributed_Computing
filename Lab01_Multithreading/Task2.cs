using System;
using System.Diagnostics;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace lab01{
    class Program{
        static void Main(string[] args){
            calculatePI();
        }
        static void calculatePI(){
            long num_step = 10000;
            double x, pi;
            var sum = new ThreadLocal<double>(true);
            double steps;
            steps = 1/((double)num_step);
            Stopwatch timer = Stopwatch.StartNew();

            Parallel.For(0,  num_step, new ParallelOptions { MaxDegreeOfParallelism = 1 }, i =>{
                x = (i + 0.5) * steps;
                sum.Value = sum.Value + 4.0 / (1.0 + x * x);
            });
            pi = steps * sum.Values.Sum();
            timer.Stop();
            sum.Dispose();
            Console.WriteLine("PI with {0} steps is {1} in {2} miliseconds ", num_step, pi, (timer.ElapsedMilliseconds));
        }
    }
}