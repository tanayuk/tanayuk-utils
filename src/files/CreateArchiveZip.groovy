package files

import java.util.zip.ZipOutputStream

public class CreateArchiveZip {
    static void main(args) {
        def cli = new CliBuilder(usage: "groovy CreateArchieZip.groovy")
        cli.h('print this message')
        cli.a(argName: 'file', required:true, 'Archive file name to be created i.e.) aaa.zip')
        cli.t(argName: 'directory/file', required:true,'Target directory/file to be archived')

        def options = cli.parse(args)

        if(options.h){
            cli.usage()
            return
        }
        def archiveFileName = "${options.p}.zip"
        ZipOutputStream zipFile = new ZipOutputStream()
    }
}
