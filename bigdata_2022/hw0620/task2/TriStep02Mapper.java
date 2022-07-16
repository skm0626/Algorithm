package task2;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import task2.IntPairWritable;

public class TriStep02Mapper extends Mapper<IntPairWritable, IntPairWritable, IntPairWritable, IntPairWritable>{
	
    IntWritable ok1 = new IntWritable();
	IntPairWritable ov1 = new IntPairWritable();
	IntWritable ok2 = new IntWritable();
    IntPairWritable ov2 = new IntPairWritable();
	
	@Override
	protected void map(IntPairWritable key, IntPairWritable value, Mapper<IntPairWritable, IntPairWritable, IntPairWritable, IntPairWritable>.Context context)
        throws IOException, InterruptedException {
		
//      ov1.set(key.get(), value.get());
      context.write(key, value);
	}
}
