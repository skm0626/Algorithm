package task2;

import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class TriStep01Reducer extends Reducer<IntWritable, IntPairWritable, IntPairWritable, IntPairWritable>{
  IntPairWritable ok = new IntPairWritable();
  IntPairWritable ov = new IntPairWritable();
//  int[] arr_sum = new int[1800000];
   
   @Override
   protected void reduce(IntWritable key, Iterable<IntPairWritable> values,
         Reducer<IntWritable, IntPairWritable, IntPairWritable, IntPairWritable>.Context context) throws IOException, InterruptedException {
      int sum=0;
      ArrayList<IntPairWritable> neighbors = new ArrayList<IntPairWritable>();
      for(IntPairWritable val : values) {
//        arr_sum[key.get()]+=1;
        sum+=1;
        String str = val.toString();
        String[] arr = str.split("\t");
        int u = Integer.parseInt(arr[0]);
        int v = Integer.parseInt(arr[1]);
        IntPairWritable k = new IntPairWritable();
//        num.set(u, v);
        k.set(u,v);
//        ov.set(a,b);
//        context.write(ok, ov);
        neighbors.add(k);
      }
      
//      String str = values.toString();
//      String[] arr = str.split("\t");
      for(IntPairWritable ne : neighbors) {
        String str = ne.toString();
        String[] arr = str.split("\t");
        int u2 = Integer.parseInt(arr[0]);
        int v2 = Integer.parseInt(arr[1]);
        if (key.get()==u2) {
//          int a = arr_sum[u2];
          int a = sum;
          int b = -1;
          ok.set(u2,v2);
          ov.set(a,b);
          context.write(ok, ov);
        }
        else if (key.get()==v2) {
          int a = -1;
//          int b = arr_sum[v2];
          int b = sum;
          ok.set(u2,v2);
          ov.set(a,b);
          context.write(ok, ov);
        }
      }
   }
}