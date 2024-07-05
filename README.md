# GD2JSON
Program to convert Geometry Dash levels to JSON.

![image](https://github.com/Lim98SE/GD2JSON/assets/73658212/b75b2bce-ed22-44cc-b20d-6a1051aa1b2c)

## How To Use

Go to [GD Colon's Save Explorer](https://gdcolon.com/gdsave/) and extract your level using the "Inner String" option. Save that to your computer and run GD2JSON. (You can click "EXTRACT YOUR LEVEL!!!" to get to the site too.)

Select your file by clicking the "Select a different file" button. Select your output file by clicking the "Change output" button.

If you want your output to be readable, enable **Beautify Output**. If you want your output to be small, disable that.

Finally, click **Convert**.

## How It Works

1. The program splits the file by every pipe character, then selects the last chunk. This removes the stuff I don't know how to parse yet. (If you know how, commit it!)
2. It splits by every semicolon, then by every other comma.
3. It uses a massive switch statement to convert numbers to their values in the file. For example: `1;4` will convert to `"id":4`.
4. It then JSON serializes that output. You're done!
