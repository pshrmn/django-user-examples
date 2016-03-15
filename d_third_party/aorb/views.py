from django.shortcuts import render, get_object_or_404

from .models import Pair
from .forms import ChoiceForm


def choice_view(request):
    if not request.user.is_authenticated():
        return render(
            request,
            'home.html'
        )
    get_new_pair = True
    # when the request is posted, save the choice
    if request.method == 'POST':
        pair = get_object_or_404(Pair, pk=request.POST.get('pair'))
        form = ChoiceForm(request.POST, initial={'pair': pair})
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        else:
            # if the form was invalid, re-render previous, otherwise
            # render a new pair
            get_new_pair = False
    if get_new_pair:
        # random pair
        pair = Pair.objects.order_by('?').first()
        form = ChoiceForm(initial={'pair': pair})
    return render(
        request,
        'aorb/choice.html',
        {
            'form': form,
            'pair': pair
        }
    )
