package task3;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class TriStep00Mapper extends Mapper<Object, Text, IntPairWritable, IntWritable> {
	
	IntPairWritable ok = new IntPairWritable();
	IntWritable ov = new IntWritable();
	
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, IntPairWritable, IntWritable>.Context context)
			throws IOException, InterruptedException {
		
		StringTokenizer st = new StringTokenizer(value.toString());
		
		int u = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());

		if (u < v) {
			ok.set(u,v); //중복 제거를 위해 key로 (key,value)보내기
			ov.set(v);
			context.write(ok, ov);
		}
		else if (u > v) {
			ok.set(v,u);
			ov.set(u);
			context.write(ok, ov);
		}
	}
}
