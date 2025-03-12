# Align Armature Bones Script

## Overview
This script aligns the bones of a selected armature to match those of another armature based on bone names. It modifies position, rotation, and scale to ensure accurate alignment.

## Installation
1. Open Blender.
2. Open the Scripting workspace.
3. Create a new script and paste the provided Python code.
4. Save the script with a `.py` extension.

## Usage
1. **Select two armatures:**
   - First, select the armature you want to align (source).
   - Then, select the reference armature (target) as the active object.
2. **Run the script:**
   - Open the Scripting workspace in Blender.
   - Load and execute the script.
3. The script will align all bones in the selected armature that have matching names in the active armature.

## Notes
- Ensure both objects are armatures.
- The script works in Edit Mode to modify bone positions.
- Only bones with matching names in both armatures will be aligned.

## Troubleshooting
- If the script does nothing, verify that both selected objects are armatures.
- Ensure you have selected exactly two armatures, with the reference armature set as the active object.

## License
This project is licensed under the MIT License. See the following terms:


# Align Armature Bones Script

## Overview
This script aligns the bones of a selected armature to match those of another armature based on bone names. It modifies position, rotation, and scale to ensure accurate alignment.

```
MIT License

Copyright (c) 2025 F1dg3t

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


