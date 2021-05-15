(require 'find-lisp)

(defun jethro/publish (file)
  (with-current-buffer (find-file-noselect file)
    (setq org-hugo-base-dir nil)
    (setq hugo-base-dir nil)
    (setq HUGO_BASE_DIR nil)
    ;; (setq org-hugo-base-dir "..")
    ;; (setq hugo-base-dir "..")
    ;; (setq HUGO_BASE_DIR "..")
    (let ((org-id-extra-files (find-lisp-find-files org-roam-directory "\.org$")))
      (org-hugo-export-wim-to-md))))

(jethro/publish "/home/dd/org/Notes/dey21_dna_origam.org")
