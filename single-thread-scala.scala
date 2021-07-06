import scala.io.Source
import java.io.File

object etl extends App {
  def gather(): List[java.io.File] = {
    val d = new File("trips")
    val files = d.listFiles.filter(_.isFile).toList.filter(_.getName.endsWith(".csv"))
    files
  }

  val t1 = System.nanoTime
  val files = gather()
  for (file <- files) {
    val f = io.Source.fromFile(file)
    for (line <- f.getLines) {
      val cols = line.split(",").map(_.trim)
      // do whatever you want with the columns here
      if (cols(12) =="member") { println("member ride found")}
    }
    f.close
  }
  val duration = (System.nanoTime - t1) / 1e9d
  println(duration)
}
