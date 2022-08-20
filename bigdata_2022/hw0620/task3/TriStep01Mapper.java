package task3;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import task3.IntPairWritable;

public class TriStep01Mapper extends Mapper<IntWritable, IntWritable, IntWritable, IntPairWritable>{
	
    IntWritable ok1 = new IntWritable();
	IntPairWritable ov1 = new IntPairWritable();
	IntWritable ok2 = new IntWritable();
    IntPairWritable ov2 = new IntPairWritable();
	
	@Override
	protected void map(IntWritable key, IntWritable value, Mapper<IntWritable, IntWritable, IntWritable, IntPairWritable>.Context context)
        throws IOException, InterruptedException {
		
      ov1.set(key.get(), value.get());
      context.write(key, ov1);
      ov2.set(key.get(), value.get());
      context.write(value, ov2);
	}
}
