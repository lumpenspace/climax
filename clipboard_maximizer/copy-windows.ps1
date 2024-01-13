internal class Program
{
    private static void Main(string[] args)
    {
        Add - Type - AssemblyName System.Windows.Forms

        $list = @

        # Read lines from console input until an empty line is entered
        do
        {
            $line = Read - Host
            if ($line - ne "") {
                $list += $line
            }
        } while ($line - ne "")

        # Add command line arguments to the list
        $list += $args

        $paths = New - Object - TypeName System.Collections.Specialized.StringCollection

        foreach ($s in $list) {
            Write - Host $s
            if ([System.IO.Path]::IsPathRooted($s))
            {
                $fullPath = $s
            }
            else
            {
                $fullPath = [System.IO.Path]::Combine([System.IO.Directory]::GetCurrentDirectory(), $s)
            }
            $paths.Add($fullPath)
        }

        [System.Windows.Forms.Clipboard]::SetFileDropList($paths)}
}