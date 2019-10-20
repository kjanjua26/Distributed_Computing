
import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;

/**
 * This class reads a list of IntWritables, and emits the average value under
 * the same key.
 * 
 * Not much to it.
 * 
 * @author Daniel Jackson, Scott Griffin
 */
public class TotalValueReducer extends MapReduceBase
implements Reducer<WritableComparable,Writable,WritableComparable,Writable>
{

	public void reduce(WritableComparable key, Iterator values,
			OutputCollector output, Reporter reporter) throws IOException {
		int count = 0;
		IntArrayWritable ratingInput = null;
		Writable[] inputArray = null;
		
		while(values.hasNext()) {

			ratingInput = (IntArrayWritable)values.next();;
			inputArray = (Writable[])ratingInput.get();; 
			
			count += ((IntWritable) inputArray[0]).get();
		}
		
		output.collect(key, new IntWritable(count));
	}

}
