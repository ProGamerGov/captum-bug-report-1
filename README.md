Test ReadMe

```
git clone https://github.com/ProGamerGov/captum-bug-report-1
cd captum-bug-report-1
pip3 install -e .

# If testing on a notebook, uncomment these 2 lines
# import sys
# sys.path.append('/content/captum-bug-report-1')
cd ..
```

These imports will fail, but I need them to not fail:

```
import captum.optim.images as images
import captum.optim.transforms as transforms

import captum.optim.reducer as reducer
import captum.optim.dataset as dataset
```
