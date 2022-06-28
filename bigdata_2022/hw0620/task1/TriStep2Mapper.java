package task1;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import task1.IntPairWritable;

public class TriStep2Mapper extends Mapper<IntWritable, IntWritable, IntWritable, IntPairWritable>{
	
    IntWritable ok1 = new IntWritable();
	IntPairWritable ov1 = new IntPairWritable();
	IntWritable ok2 = new IntWritable();
    IntPairWritable ov2 = new IntPairWritable();
	
	@Override
	protected void map(IntWritable key, IntWritable value, Mapper<IntWritable, IntWritable, IntWritable, IntPairWritable>.Context context)
        throws IOException, InterruptedException {
		
//		StringTokenizer st = new StringTokenizer(value.toString());
//		
//		int u = Integer.parseInt(st.nextToken());
//		int v = Integer.parseInt(st.nextToken());

//		if (u < v) {
//			ok.set(u,v);
//			ov.set(v);
//			context.write(ok, ov);
//		}
//		else if (u > v) {
//			ok.set(v,u);
//			ov.set(u);
//			context.write(ok, ov);
//		}
//		ok1.set(u);
//		ov1.set(u, v);
//		context.write(ok1, ov1);
//		ok2.set(v);
//        ov2.set(u, v);
//        context.write(ok2, ov2);
      ov1.set(key.get(), value.get());
      context.write(key, ov1);
      ov2.set(key.get(), value.get());
      context.write(value, ov2);
	}
}
