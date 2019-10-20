
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;

/**
 * Driver class for PolyHadoop project. Runs the Hadoop instance, setting
 * up the Map/Reduce classes, input/output paths, and the Key/Value classes.
 * 
 * This does not use a Combiner class - it would add complexity to reduce
 * (necessitating a weighted average), for little to no gain. In the common
 * case, a user will only rate a movie once, and each MapTask probably operates
 * on a single data file at a time.
 * 
 * Invoke with 2 arguments, or 1.
 * 
 * @author Daniel
 *
 */
public class HadoopDriver {

	public static void main(String[] args) {
		/* Require args to contain the paths */
		/*if(args.length != 1 && args.length != 2) {
			System.err.println("Error! Usage: \n" +
					"HadoopDriver <input dir> <output dir>\n" +
					"HadoopDriver <job.xml>");
			System.exit(1);
		}*/
		
		JobClient client = new JobClient();
		JobConf conf = null;
		
		//if(args.length == 2) {
			conf = new JobConf(HadoopDriver.class);
			
			/* Pull input and output Paths from the args */
			/* Pull input and output Paths from the args */
			FileInputFormat.addInputPath(conf, new Path("/Users/Janjua/Desktop/BSCS/Semester 7th/Distributed Computing/Labs/Lab03/input/"));
			FileOutputFormat.setOutputPath(conf, new Path("/Users/Janjua/Desktop/BSCS/Semester 7th/Distributed Computing/Labs/Lab03/out2/"));
	
			/* Set to use Mapper and Reducer classes */
			conf.setMapperClass(UserRatingMapper.class);
			conf.setCombinerClass(UserRatingMapper.class);
			conf.setReducerClass(TotalValueReducer.class);

			/* UserRatingMapper outputs (IntWritable, IntArrayWritable(Writable[2])) */
			conf.setMapOutputKeyClass(IntWritable.class);
			conf.setMapOutputValueClass(IntArrayWritable.class);
			
			/* TotalValueReducer outputs (IntWritable, IntWritable) */
			conf.setOutputKeyClass(IntWritable.class);
			conf.setOutputValueClass(IntWritable.class);
			
			conf.set("mapred.child.java.opts", "-Xmx4g");
		//} else {
		//	conf = new JobConf(args[0]);
		//}
		
		client.setConf(conf);
		try {
			JobClient.runJob(conf);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
