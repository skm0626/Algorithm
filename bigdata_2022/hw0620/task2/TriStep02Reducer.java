package task2;

import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class TriStep02Reducer extends Reducer<IntPairWritable, IntPairWritable, IntWritable, IntWritable>{
  IntWritable ok = new IntWritable();
  IntWritable ov = new IntWritable();
  int a=-1;
  int b=-1;
   
   @Override
   protected void reduce(IntPairWritable key, Iterable<IntPairWritable> values,
         Reducer<IntPairWritable, IntPairWritable, IntWritable, IntWritable>.Context context) throws IOException, InterruptedException {

      ArrayList<IntPairWritable> neighbors = new ArrayList<IntPairWritable>();
      for(IntPairWritable val : values) {
        String str = val.toString();
        String[] arr = str.split("\t");
        int u = Integer.parseInt(arr[0]);
        int v = Integer.parseInt(arr[1]);
        if (u!=-1) {
          a=u;
        }
        if (v!=-1) {
          b=v;
        }
//        neighbors.add(val);
      }

        String str = key.toString();
        String[] arr2 = str.split("\t");
        int u2 = Integer.parseInt(arr2[0]);
        int v2 = Integer.parseInt(arr2[1]);
        if (u2>v2 || a>b) {
          ok.set(v2);
          ov.set(u2);
          context.write(ok, ov);
        }
        else if (a<=b) {
          ok.set(u2);
          ov.set(v2);
          context.write(ok, ov);
        }
   }
}