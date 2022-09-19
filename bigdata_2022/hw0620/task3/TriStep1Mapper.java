package task3;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class TriStep1Mapper extends Mapper<IntWritable, IntWritable, IntWritable, IntWritable> {
	
	IntWritable ok = new IntWritable();
	IntPairWritable ov = new IntPairWritable();
	
	@Override
	protected void map(IntWritable key, IntWritable value, Mapper<IntWritable, IntWritable, IntWritable, IntWritable>.Context context)
			throws IOException, InterruptedException {
		
	    context.write(key, value);
//		if (key.get() < value.get()) {
////			ok.set(key.get());
////			ov.set(key.get(), value.get());
//			context.write(key, value);
//		}
//		else if (key.get() > value.get()) {
////			ok.set(value.get());
////			ov.set(value.get(),key.get());
//			context.write(value, key);
//		}
	}
}
